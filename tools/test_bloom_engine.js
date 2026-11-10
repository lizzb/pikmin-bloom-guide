// Tests for the planner's logic. Run: node tools/test_bloom_engine.js
// Pulls the engine out of bloom-planner.html (between the ENGINE markers) so there is one copy of the logic.
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'bloom-planner.html'), 'utf8');
const src = html.split('/*ENGINE-START*/')[1].split('/*ENGINE-END*/')[0];
const E = new Function(src + '; return {SPECIES,speciesByName,colorsOf,plantingModel,buildCtx,makePlans,evalPlan,findInit,ranges,tally,tipOf,check,whiteTries,SLOTS,COLORS};')();

let pass = 0, fail = 0;
const t = (name, ok, extra) => { if (ok) pass++; else { fail++; console.log('FAIL', name, extra ?? ''); } };

// Inventory helper: flowers directly (fpp = 1, ppn = 1) so counts equal flowers.
const inv = o => { const r = {}; for (const s of E.SLOTS) r[s] = { p: o[s] || 0, n: 0 }; return r; };
const plansFor = (sp, T, o) => {
  const ctx = E.buildCtx(sp, T, inv(o), 1, 1);
  const plans = E.makePlans(ctx).map(p => { if (p.usable === false) return p; const v = E.findInit(p, ctx); return v ? { ...p, vals: v, usable: true } : { ...p, usable: false, reason: 'no init' }; });
  return { ctx, plans, byId: id => plans.find(p => p.id === id) };
};
const allocOf = (r, id) => { const p = r.byId(id); return E.evalPlan(p, p.vals, r.ctx).alloc; };

// --- Species table sanity
t('54 species', E.SPECIES.length === 54, E.SPECIES.length);
for (const s of E.SPECIES) {
  const sum = Object.values(s.odds).reduce((a, b) => a + b, 0);
  t('odds sum ~100 ' + s.name, Math.abs(sum - 100) < 0.01, sum);
}

// --- Your examples from the flowchart notes
let r = plansFor('Salvia', 'W', { 'S:W': 200, 'O:W': 200, 'O:R': 200, 'O:B': 200, 'O:Y': 200 });
let a = allocOf(r, 'W1');
t('W1 uses 156 white salvia', a['S:W'] === 156, a);
t('W1 total 300', E.tally(a).total === 300);
t('W1 no colour over 100', Math.max(a['O:R'] || 0, a['O:B'] || 0, a['O:Y'] || 0) <= 100, a);

// White fallback: no white salvia, red/blue/yellow salvia + white others => 52/52/52 + 144 white
r = plansFor('Salvia', 'W', { 'S:R': 100, 'S:B': 100, 'S:Y': 100, 'O:W': 200 });
t('W1 unusable without white salvia', !r.byId('W1').usable);
a = allocOf(r, 'W2');
t('W2 gives 52/52/52 + 144 white', a['S:R'] === 52 && a['S:B'] === 52 && a['S:Y'] === 52 && a['O:W'] === 144, a);

// Non-white branch 1: 156 red salvia + 144 white
r = plansFor('Salvia', 'R', { 'S:R': 200, 'O:W': 200 });
a = allocOf(r, 'N1');
t('N1 156 red salvia + 144 white', a['S:R'] === 156 && a['O:W'] === 144, a);

// Branch 2: 144 yellow salvia + 12 red salvia + 144 red
r = plansFor('Salvia', 'R', { 'S:R': 20, 'S:Y': 200, 'O:R': 200 });
t('N1 unusable (only 20 red salvia)', !r.byId('N1').usable);
a = allocOf(r, 'N2');
t('N2 144 yellow + 12 red salvia + 144 red', a['S:Y'] === 144 && a['S:R'] === 12 && a['O:R'] === 144, a);

// Branch 3: 80 yellow salvia + 80 blue salvia + 140 red
r = plansFor('Salvia', 'R', { 'S:Y': 80, 'S:B': 80, 'O:R': 200 });
a = allocOf(r, 'N3');
t('N3 yields species 156-198 and red filler', (a['S:Y'] + a['S:B']) >= 156 && (a['S:Y'] + a['S:B']) <= 198 && a['S:Y'] <= 99 && a['S:B'] <= 99, a);
t('N3 total 300', E.tally(a).total === 300);

// Branch 4: 156 white salvia + 144 red
r = plansFor('Salvia', 'R', { 'S:W': 200, 'O:R': 200 });
a = allocOf(r, 'N4');
t('N4 156 white salvia + 144 red', a['S:W'] === 156 && a['O:R'] === 144, a);

// Dead end
r = plansFor('Salvia', 'R', { 'S:W': 10, 'O:R': 50 });
t('dead end has no usable plan', r.plans.every(p => !p.usable));

// White dead end (not enough species)
r = plansFor('Salvia', 'W', { 'S:W': 20, 'O:W': 200 });
t('white with 20 species is a dead end', r.plans.every(p => !p.usable));

// Single-colour species
r = plansFor('Sunflower', 'Y', { 'S:Y': 300 });
t('sunflower single plan', r.byId('SV') && r.byId('SV').usable);
r = plansFor('Sunflower', 'R', { 'S:Y': 300 });
t('sunflower red has no plans', r.plans.length === 0);

// Tip logic from Pikipedia examples
t('tip: 40W+30R reads red', E.tipOf({ W: 40, R: 30, B: 0, Y: 0 }, 70) === 'R');
t('tip: 40W+30R+20Y+20B reads ???', E.tipOf({ W: 40, R: 30, B: 20, Y: 20 }, 110) === '?');

// Reddit trap: 156 white + 144 red must NOT be an acceptable white plan
const ctxW = E.buildCtx('Salvia', 'W', inv({}), 1, 1);
t('156W+144R rejected for white', !E.check({ 'S:W': 156, 'O:R': 144 }, ctxW).every(x => x.ok));

// Randomised: every plan we hand out is valid and each slider range contains its value
let rnd = 12345; const R = () => (rnd = (rnd * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
let produced = 0;
for (let i = 0; i < 400; i++) {
  const sp = E.SPECIES[Math.floor(R() * E.SPECIES.length)];
  const cols = E.colorsOf(sp); const T = cols[Math.floor(R() * cols.length)];
  const o = {}; for (const s of E.SLOTS) o[s] = R() < 0.6 ? Math.floor(R() * 260) : 0;
  const rr = plansFor(sp.name, T, o);
  for (const p of rr.plans.filter(p => p.usable)) {
    produced++;
    const ev = E.evalPlan(p, p.vals, rr.ctx);
    t(`valid ${sp.name}/${T}/${p.id}`, ev.ok, ev.rules.filter(x => !x.ok));
    t('300 total', E.tally(ev.alloc).total === 300);
    const rg = E.ranges(p, p.vals, rr.ctx);
    for (const a2 of p.adj) t('range holds value', rg[a2.key][0] <= p.vals[a2.key] && p.vals[a2.key] <= rg[a2.key][1]);
    // moving a slider to either end of its range keeps the plan valid
    for (const a2 of p.adj) for (const e of rg[a2.key]) t('range end valid', E.evalPlan(p, { ...p.vals, [a2.key]: e }, rr.ctx).ok);
  }
}
t('random run produced plans', produced > 50, produced);

// Planting model: squad 40 at 5 km/h should give about 100 flowers per 80 m pass (Reddit report)
const M = E.plantingModel(40, 5, 1, 0);
t('40 Pikmin pass ~96', Math.abs(M.passFlowers - 96) < 1, M.passFlowers);
const M2 = E.plantingModel(40, 5, 0.85, 0);
t('fpp sane', M2.fpp > 10 && M2.fpp < 20, M2.fpp);

console.log(`${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
