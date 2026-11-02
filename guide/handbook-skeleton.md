# Pikmin Bloom Handbook (skeleton, v0)

Restructure of [overview.md](overview.md). Drafted 2026-11-01. Facts are tagged so you can skim past them and still know how far to trust them.

**Legend** (tags sit at the end of a line)

| Tag | Meaning |
|---|---|
| ✅ | Confirmed: Discord FAQ, official Help Center/news, or tested by lizz |
| 🟡 | Probable: wiki or recent community notes, not independently verified |
| ❓ | Unconfirmed, conflicting, or opinion |
| 🕰️ | Possibly outdated (2021-2024 sources) |

Source letters: **D** Discord #faq ([discord-faq.md](discord-faq.md)) · **H** official Help Center/news · **W** Pikipedia wiki · **R** Reddit notes pasted into overview.md · **L** lizz's own testing · **C** calculated here from the cited numbers.

Trust order when sources disagree: D > H > W > R, and newer beats older. `🚧 migrate` lines mark content still sitting in overview.md.

---

## 0. TL;DR and daily checklist

- Walk, plant flowers, raise Pikmin. Monthly **Event Challenges** are the only real "goal" system. ✅H
- Free daily: gift from Shop, detector. 🟡R 🕰️
- Only feed special nectar to **budded** Pikmin (2 petals per nectar). 🟡W
- Keep your squad full and hands empty while planting. 🟡R
- Do your mushrooms each day; don't collect month-end mushrooms until the 1st if you want new-month nectar. ✅D
- Spend coins on **Pikmin storage** first. ✅D
- Releasing is normal; the decor list stays filled after release. ✅D

🚧 migrate: F2P daily guide (overview.md L101-108), core loop (L110-121)

---

## 1. Pikmin storage and releasing (300 cap, free-to-play)

- **Limit:** starts at 300. ✅H Shop upgrades raise it to 4,500 max. 🟡H (older announcements quoted 3,000 / 3,200 / 4,000 caps, so check the in-app number.) ❓
- **No free way to expand** is documented. ✅H
- **Sorting:** Discovery Date, Favorite, Type, Friendship, Decor Category. 🟡R Search box (magnifier) takes terms like `bloom` or a heart range. ✅D
- Spend coins on storage first; extra room lets you keep full single-colour squads for elemental mushrooms. ✅D

### What to release (in order)
1. Duplicates of decor you already have. ✅D
2. Old event Pikmin. Returning decor gets only a small boost, and there is no guarantee event Pikmin return. ✅D
3. Ones you don't think are cute. ✅D
4. Plain, weak, unneeded regular Pikmin. 🟡R

### What to keep
- Anything in a **rare-decor category** until you've unlocked rare decor, because releasing earns points. ✅D (see §3)
- Your strongest Pikmin. Purple has the best base attack, and the mushroom squad cap is 40. ✅D
- Favourites: lifelog memories, special-location decor. ❓R

### Seasonal decor: discard at month end?
- **Mostly no need to keep it for the collection.** Once a decor is filled in on the Decor Pikmin list, it stays filled even if released. ✅D
- Reasons to keep one: you want the attack boost for that month's event mushrooms, or it sits in a rare-eligible category. ❓
- Don't count on reruns. Event Pikmin may not return, though some community members expect reruns. ❓R
- Older advice in this repo said "keep one of each"; the dex-persistence fact above makes that weaker. Keep one only if slots are spare.

### What you get for releasing
- **10 petals.** ✅L
- Only common petals, e.g. releasing a Pikmin fed a red hibiscus gives plain red, not red hibiscus. ❓ (lizz suspects this but may have been unlucky; see Open Questions for a test)
- Rare-decor points: 5 without decor, 20 with decor. ✅D

### Decor-tracking tips
- Name the first Pikmin of each decor so you know which to keep. ✅D (nickname by pluck order, since Date Plucked isn't shown)
- Sort by Decor Category on both the Pikmin and Seedling screens. Order is: decor type, then Red - Yellow - Blue - Purple - White - Pink - Gray - Ice - Huge, then date. ✅D
- Icon behind a Pikmin: **yellow** = you already own that colour + decor, **gray** = not yet. ✅D A yellow-icon seedling can't add a new dex entry. 🟡C
- Special event decor shares one category; the icon is yellow only when all of it is collected. ✅D

🚧 migrate: duplicate-decor identification (overview.md L288-301, L453)

---

## 2. Decor Pikmin and finding decor

- **Where decor comes from:** the type of place where you found the seedling (OpenStreetMap and Foursquare data). ✅D
- **Standard seedling:** reach 4 hearts, then it makes a gift trip back to its origin and returns as a decor Pikmin. ✅D
- **Huge and Gold seedlings** hatch with decor. ✅D
- **Finders:** [pikmin-map.pixelpirate.fr](https://pikmin-map.pixelpirate.fr/), [decor-pikmin-finder](https://decor-pikmin-finder.vercel.app/). May not match the game exactly. ✅D
- **Lifelog photo trick:** a photo entry can trigger a seedling expedition at that location if the spot is unoccupied, you haven't already triggered one that day, and it's within 10 km of where you travelled. ✅D
- **Luck:** seedling type is random. See the Pikmin Luck Calculator and the coupon-collector problem. ✅D
- **Pikmin size** differences are cosmetic. ✅D

---

## 3. Collecting all rare decor

### Rules
- **Eligible categories** (rare unlocked as of the date shown) ✅D:

| Category | Since |
|---|---|
| Restaurant, Waterside, Bakery, Hair salon | launch set |
| Supermarket (banana) | 2025-06-13 |
| Coffee cup | 2025-09-12 |
| Roadside (coin) | 2025-11-01 |
| Park (clover and four-leaf clover) | 2026-03-13 |
| Ice Park | 2026-04-10 |
| Pharmacy | 2026-06-12 |
| Stadium, Train (ticket) | 2026-07-10 |
| Ice Toothbrush, Ice Stadium, Ice Ticket | 2026-08-07 |

- **Unlock:** collect every base Pikmin in the category: 7 or 8 for most, 14 for supermarket, 32 for roadside, 16 for park. ✅D Once unlocked, new base Pikmin added later don't undo it. ✅D
- **Earn points** by growing, getting decor, or releasing a Pikmin in that category. ✅D
- **Reward:** at a threshold, pick one normal decor Pikmin in the category to collect a gold present and become the rare version. ✅D The rare Pikmin keeps its original geotag. ✅D
- **Points** ✅D:

| Action | Points |
|---|---|
| Pluck seedling | 30 |
| Release without decor | 5 |
| Release with decor | 20 |
| Decor from gift | 200 |
| Pluck Huge seedling | 200 |

- **Thresholds:** 800, 1,200, 3,000, 5,000, 5,000; level 6+ presumably 5,000. ✅D for 1-5, ❓D for 6+

### Cost to collect (from the points above)
The friendship cost is 212 points to reach 4 hearts. 🟡W With the 5th-feed trick (4 feeds at 1, one at 11) that is about 71 nectar. 🟡C

| Route | Points each | Cost |
|---|---|---|
| Pluck and release at once | 35 | Steps only (1,000 to 5,000 each), no nectar, no slot held |
| Raise to 4 hearts, then release | 250 | Same steps + ~71 nectar + gift trip + a held slot |
| Huge seedling, then release | ~220 | 10,000 steps, no nectar |

| Cumulative points | Instant release | Raise, then release | Huge, then release |
|---|---|---|---|
| 800 (1st) | 23 seedlings | 4 Pikmin, ~284 nectar | 4, 40k steps |
| 2,000 (2nd) | 58 | 8, ~568 | 10, 100k |
| 5,000 (3rd) | 143 | 20, ~1,420 | 23, 230k |
| 10,000 (4th) | 286 | 40, ~2,840 | 46, 460k |
| 15,000 (5th) | 429 | 60, ~4,260 | 69, 690k |

All rows 🟡C. **Unlocking a category** costs extra: expected seedlings needed ≈ n × H(n) for a set of n: about 18 for 7, 22 for 8, 46 for 14, 54 for 16, 130 for 32. ❓C (assumes every type is equally likely, which the game doesn't promise)

### Strategy
1. **Before unlock:** raise gray-icon Pikmin to 4 hearts; release yellow-icon ones at once. 🟡C
2. **After unlock:** raise rare-category Pikmin if you have nectar and slots, because it earns about 7x the points. Release everything else. 🟡C
3. **Never release a rare-category Pikmin without decor** if you can raise it first. 5 points against 220+.
4. Huge seedlings are free release fodder (200 + 20 points).
5. Releasing is also your storage management, so the points come as a side effect.

### Unconfirmed
- Number of rare Pikmin per category, so no grand total. ❓
- Whether a Huge seedling's 200 replaces or adds to the 30. ❓
- Whether gold seedlings count toward points. ❓
- Whether the rare gift trip itself earns the 200. ❓
- Whether progress carries across levels or resets. ❓

---

## 4. Friendship and feeding

- **Friendship from** ✅D: nectar 1 / 10 / 53 points; expedition 1; in squad while planting 1 per day; mushroom battle 3 (large non-elemental 8; large elemental or giant 10).
- **4 hearts** makes a standard seedling eligible for its decor gift trip. ✅D
- **Heart sizes:** a red heart takes 53 points, so 4 hearts is 212. 🟡W
- **5th-feed bonus:** feeding a Pikmin that has had 4 petals plucked gives +10 on top of the usual 1. 🟡W Other notes count the feeds differently (5 vs 6). ❓R
- **Nectar-efficient loop:** feed to the 5th feed, don't collect that last petal, wait 2 hours for the counter to reset, repeat. 🟡W/R
- **Time-efficient loop:** pluck all 6 to bare, walk ~1,800 steps to regrow a leaf, repeat. Doesn't work 9 pm to 4 am. 🟡W
- **Maturity timers:** bare to leaf 6 h, leaf to bud 8 h, each step takes 12 s off (1,800 and 2,400 steps); only squad Pikmin get the leaf timer reduction. 🟡W
- **Daily reset:** 4:00 AM local, every Pikmin back to leaf. 🟡W
- Pikmin don't get sad or leave if you don't feed them. 🟡R
- **Attack power by state:** bare 0, leaf +1, bud +2, flower +3, seasonal +4, current flower of the month +5. 🟡W
- Don't feed at 4 gold hearts unless you need the flower for a mushroom. 🟡R

🚧 migrate: feeding Q&A cleanup (overview.md L66-99, L580-637, L669-696, L705-737)

---

## 5. Nectar, petals, fruit

- **Nectar:** from fruit (walking, expeditions, mushrooms, planting near Big Flowers) and weekly step challenges. 🟡W
- **Petals:** from feeding nectar then plucking a glowing flower, blooming, release (10 ✅L), weekly flower challenge, shop. 🟡W
- **Caps:** 200 per type default, expandable with real money. 🟡R 🕰️
- **Budded Pikmin** give 2 petals for 1 nectar. 🟡W Leaf to bud: feed 1 white nectar or walk ~2,400 steps. 🟡W
- **Fruit:** one small fruit per Pikmin; large fruit needs up to 12 carriers; elemental and event fruit sizes differ. 🟡W
- **Large fruit nectar:** floor(mass/10), plums floor(mass/8). 🟡W

🚧 migrate: fruit tables (overview.md L490-534)

---

## 6. When you're short on nectar or petals for an Event Challenge

**What Pikmin Bloom calls them:** *Event Challenges*, unlocking at level 5, with a paid **Premium Event Pass** (level 20+) that adds extra seasonal nectar per stage. ✅H (the "season pass" name comes from Reddit, not the game.)

Roughly in order of cost; the order is my judgement. ❓C

1. **Check which species you need.** Sources that give a specific species, per D ✅:
   - Big Flower blooming (any in-season species, incl. event flowers).
   - Mushroom battles.
   - Instabloom (primary/secondary species of the month only).
   - Weekly challenges (primary/secondary).
   - Community Day: plain flowers bloom as the flower of the month.
   - The shop.
2. **Feed buds, not leaves.** Same nectar gives 2 petals. 🟡W
3. **Weekly challenges every week.** Step challenge gives each of the 4 regular nectars, and the planting challenge gives the month's petals. ✅D Rewards are set on Monday and don't change if the month ends mid-week. ✅D
4. **Mushrooms with timing:** reward collection time decides which month's nectar you get. Don't tap Collect on a month-end mushroom until the 1st. ✅D Event mushrooms drop old and current species. 🟡R
5. **Instabloom** a Big Flower: 150 petals of one type (unbloomed), 80 (already bloomed). ✅D Unbloomed gives a token of nectar (7 in one test); the postcard shows the petals you used. ✅D
6. **Release spare Pikmin for 10 petals.** ✅L Species uncertain. ❓
7. **Premium Event Pass** extra seasonal nectar per stage. ✅H
8. **Don't waste petals on planting.** Use a single-petal pulse every 5 minutes while stationary. ✅D
9. **Buy petals with coins** as a last resort; prices from 2021 (white 50, yellow 150, red 180, blue 200 for 180). 🕰️R
10. **Store old seasonal nectar and petals** at the end of each event; they come back as secondaries the next year. 🟡R
11. **Event currency** also comes from planting (1 per 100 flowers, no limit) and event mushrooms. ✅D

Also: stages that overflow your storage can be released or received later; unclaimed rewards are released when the event ends. ✅H

---

## 7. Mushrooms

- **Join:** first 5 players are free; 6th onward need a Mushroom Recharge Ticket. ✅D
- **Bullhorn:** 1 per day, up to 3 on Giant Weekends; not saved overnight; you can edit the invite list until a friend responds. ✅D
- **Min AP rule:** a host's "3k AP min" means you must *add* at least that much AP. A max AP request is for slow cooking. ✅D
- **Slow cooking:** deliberately slow mushrooms, mainly so month-end ones finish in the next event. ✅D
- **Reset:** untouched mushrooms reset daily at 18:00 UTC; from Oct 5 that becomes 3 am your local time. ✅D (year not stated) A defeated one respawns after 5 minutes. ✅D
- **Event box:** the mushroom type sets the mystery box/currency. Old event mushrooms give none once the event ends. ✅D
- **Stars on a normal event mushroom don't change the rare box chance.** ✅D
- **Seedlings from mushrooms:** no longer possible. ✅D
- **Max participants:** small 25, normal 30, large 35, giant 40. 🟡R 🕰️
- **Elemental:** send only the matching type. ✅D
- **More nectar:** join or host with extra players; 4-star large regular beats large elemental. ✅D

🚧 migrate: attack power tips, October 2026 event notes (overview.md L1041-1079, date-stamped, move to an events page)

---

## 8. Planting flowers and Big Flowers

- Planting area reaches its max at level 55. ✅D
- It's based on distance, not steps or time; up to 20 km/h. ✅D
- Don't return to the same area within 5 minutes. ✅D
- Stationary: single-petal pulse every 5 minutes. ✅D
- Squad of 40 at level 55 gives the biggest area. ✅D
- **Big Flower:** 40 m radius. After it blooms, plant 1 more flower within the first hour to trigger the fruit expedition. ✅D
- **Coins from planting:** conflicting numbers in notes (1 per 500, max 30 vs 1 per 250, max 60). ❓R

🚧 migrate: planting table (overview.md L873-879)

---

## 9. Social: friends, postcards, party walks

- **Friend cap:** 650 across all Niantic games (since 2026-01-13). ✅D

### Postcards
- **Point:** none for gameplay; they're a collectible and a gift. ✅D
- **Sending:** the Pikmin and postcard travel 12 hours, whatever the distance. ✅D✅W
- **Return:** the Pikmin returns right after your friend receives it; if the friend is inactive, 2 days. ✅D
- **Cooldown:** one postcard per friend per 24 hours. 🟡W
- **Storage:** 400 to start. 🟡W
- **Friendship:** a Pikmin sent to retrieve a postcard gets 1 point. 🟡W
- Postcards can be traded on the Discord boards. ✅D

### Party walks
- **Point:** a shared walk with friends. Regular ones have no goal and no completion reward, but give each participant a **Memento Card** saved to that day's lifelog. 🟡W
- **Official walks** sometimes give items (e.g. 30 Blue Hibiscus petals in May 2026, seedlings in April 2026). ✅H
- **Limits:** host 1 at a time, join up to 3 (official ones don't count); duration 2 hours to 28 days. 🟡W
- With 5+ participants the game may suggest friend requests. 🟡W

---

## 10. Shop and coins

- **What to spend coins on, in order** ✅D: Pikmin storage; nectar storage (a budded Pikmin turns 1 nectar into 2 petals, so it's better value than petal storage); mushroom tickets; Mii costumes / postcard storage; completion tickets for decor gaps.
- Nectar vs petal storage is still argued in the notes. ❓R
- Slot, step-tank, and petal prices in overview.md are 2021 figures. 🕰️

🚧 migrate: overview.md L1228-1266

---

## 11. Misc facts

- Roulette reward is fixed; tap timing doesn't matter. ✅D
- Spoofing/flying is banned on the Discord server and against Niantic's ToS. ✅D
- Name colours: `<color=#hexcode>name</color>`, 30 characters max including code, names can't change for a week; names ending in "a" fail the filter. ✅D
- Mii not updating: switch to a default Mii, save, switch back. ✅D

---

## Open questions

- [ ] Does release always give plain-colour petals? **Test:** feed a Pikmin one seasonal nectar, release, check which jar goes up by 10. Repeat about 5 times. (lizz)
- [ ] Rare decor: points per category, Huge seedling 200 vs 230, gold seedlings, level carry-over (§3)
- [ ] Seedling unlock levels: overview.md has two conflicting tables (L259-262 vs L1363-1367)
- [ ] Mushroom unlock level: 9, 12, or 15?
- [ ] Coins from planting (§8)
- [ ] Do step slots share steps across seedlings or split them?
- [ ] Do Party Walk steps do anything beyond the Memento Card? (§9)
- [ ] Is the 3 am mushroom reset in effect now (the FAQ says "from Oct 5")?

## Provenance
Discord #faq copied 2026-11-01. Reddit threads referenced in overview.md could not be fetched, so R-tagged items come only from the notes already pasted there.
