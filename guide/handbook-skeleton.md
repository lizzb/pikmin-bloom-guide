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
- Only feed special nectar to **budded** Pikmin (2 petals per nectar). ✅L
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
Every rule uses something you can see on screen.
1. **Same colour + decor you already own.** Sort by Decor Category, nickname the first of each, release later copies. ✅D A yellow icon on a seedling means you already own that colour + decor. ✅D
2. **Old event decor** from an event that has ended. Returning decor gets only a small boost, and there is no guarantee event Pikmin return. ✅D
3. **Lowest friendship first:** sort by Friendship Level, ascending, and release from the bottom. Skip rare-eligible categories (§3) and any Pikmin you're raising to 4 hearts. 🟡C
4. **No decor and under 4 hearts** in a non-rare category. 🟡C

### What to keep
- Anything in a **rare-decor category** until you've unlocked rare decor, because releasing earns points. ✅D (see §3)
- Your mushroom squad: highest hearts, and Purple first (best base attack). The squad cap is 40, and elemental mushrooms take one colour only, so keep full single-colour sets. ✅D

### Seasonal decor: discard at month end?
- **Mostly no need to keep it for the collection.** Once a decor is filled in on the Decor Pikmin list, it stays filled even if released. ✅D
- Reasons to keep one: you want the attack boost for that month's event mushrooms, or it sits in a rare-eligible category. ❓
- Don't count on reruns. Event Pikmin may not return, though some community members expect reruns. ❓R
- Older advice in this repo said "keep one of each"; the dex-persistence fact above makes that weaker. Keep one only if slots are spare.

### What you get for releasing
- **10 basic petals** ✅L ✅W, in the colour of the nectar the Pikmin was fed most recently; white if it never got nectar. 🟡W This matches lizz's observation: a Pikmin fed red hibiscus gives plain red petals, not red hibiscus.
- Rare-decor points: 5 without decor, 20 with decor. ✅D

### Keeping one of every Pikmin?
- You don't need to, for the collection: the decor list stays filled after release. ✅D
- **No official total exists** for decor Pikmin. A Feb 2026 guide says 116 types / 833 decor Pikmin, but the passage is garbled. ❓ An older wiki figure was 400+ across 60+ sets. 🕰️
- **The wiki lists 40 location categories**, each with up to 8 colour variants (Red, Yellow, Blue, Purple, White, Winged, Rock, Ice). 🟡W Roadside alone is 32. ✅D So the regular set alone is likely past 300. ❓C
- **Live-event sets:** 18, per the wiki (Super Mario Keychain, Present Sticker (Gold), Chess Piece, Photo Button Badge, ...). Some re-run (e.g. Ice Cream: Classic in 2024, 2025, 2026). 🟡W Monthly in-app event sets (chocolate, spring sticker, klompen keychain, playing cards at 14 types) are on top. ✅H
- **Starting in June 2026:** regular decor is available any time, so the missing piece is only events before June that haven't re-run. My estimate is roughly 600-830 slots for one of everything, tied to the 833 figure above. ❓C (I can't make this tighter without a real count.)
- **Rules that apply:** 300 slots by default; one per colour + decor; you can't obtain an expired event set again unless it re-runs (e.g. Afternoon Tea in March 2026). ✅H

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
- **Pikmin size** varies slightly; it is cosmetic and doesn't affect gameplay. ✅D

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
- **Check how many times a Pikmin has been fed:** double-tap it to see how many consecutive petal collections you've made. ✅H (read via search summary; press-and-hold in Reddit notes is unconfirmed ❓). A glowing Pikmin has one feed pending, so fed = shown + 1, except white nectar on a leaf, which makes a bud and gives no petals. 🟡C
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
- **Caps:** petals start at 300 per type (they were 200 before 2022-07-11), expandable with real money. 🟡W Nectar cap: notes say 200 🕰️R, but it may have been raised with petals. ❓
- **Budded Pikmin** give 2 petals for 1 nectar. ✅L Leaf to bud: feed 1 white nectar or walk ~2,400 steps. 🟡W
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
2. **Feed buds, not leaves.** Same nectar gives 2 petals. ✅L
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

### Which size to pick (small / normal / large / giant)
You get 3 free battles a day, so pick the biggest one your group can reach 3 stars on. 🟡C

| Size | Red HP | Min Pikmin | Max players |
|---|---|---|---|
| Small | 87,400 | 1 | 25 |
| Normal | 670,600 | 10 | 30 |
| Large | 2,916,000 | 15 | 35 |
| Giant | 3,499,200 | 20 | 40 |

🟡W. Stars and rewards (Red): ✅W for the thresholds, 🟡C for nectar totals (from the fruit ranges in overview.md)

| | 3 stars | 4 stars |
|---|---|---|
| **Small** | 1,080 AP: 5 cherries + postcard | 2,240 AP: 2 cherries + apple + postcard (~25-60 nectar) |
| **Large** | 4,050 AP: 4 peaches + postcard (~80-185) | 5,600 AP: 3 watermelons + peach + special fruit + postcard (~190-410 + 1 special) |

- Score is total attack power plus a 5%, 10%, 15% or 20% time bonus; join early. ✅W
- Matching colour doubles attack power. ✅W
- A 4-star large regular mushroom gives an extra coloured fruit compared with a large elemental. ✅D
- Choose by **what you need**: event mushrooms for event currency, colour mushrooms for a nectar colour (the Discord nectar-ping roles announce them). ✅D
- **Small is only worth it** when you're solo, below ~2,000 AP, or you need a quick 3 stars for a mission. Otherwise it pays roughly a seventh as much nectar. 🟡C
- I could not read the normal and giant reward rows in full. ❓

🚧 migrate: attack power tips, October 2026 event notes (overview.md L1041-1079, date-stamped, move to an events page)

---

## 8. Planting flowers and Big Flowers

### What counts as "the same area"
- The world is a grid of cells about **5 x 5 m**. One flower per cell, and a cell can't be replanted for **5 minutes**. ✅W
- Flowers land in a rectangle of cells around you. Its size steps up with squad size ✅W (metres are my conversion, 🟡C):

| Squad | Min level | Cells | About | Petals/min | A petal every |
|---|---|---|---|---|---|
| 1-9 | 1 | 2x1 (2) | 10 x 5 m | 2 | 30 s |
| 10-19 | 7 | 3x2 (6) | 15 x 10 m | 3 | 20 s |
| 20-29 | 9 | 4x3 (12) | 20 x 15 m | 4 | 15 s |
| 30-39 | 15 | 5x4 (20) | 25 x 20 m | 5 | 12 s |
| 40 | 55 | 6x5 (30) | 30 x 25 m | 6 | 10 s |

- **Your 2.5 m back-and-forth path:** every pass lands in cells you just planted, so nothing new grows until 5 minutes pass. ❓C
- **To avoid wasting petals,** separate the two legs by at least the footprint width across your direction of travel: 5 m for a squad under 10, up to 25 m at 40. Use the larger number plus a few metres for GPS jitter. ❓C (the wiki is inconsistent about which axis is longer, and whether the area is centred on you)
- **Simplest rule:** don't return to the same area within 5 minutes. ✅D A loop of about 5 minutes (roughly 400 m at 5 km/h) does that.

### Does the rate change with phone state?
- Planting continues with the app closed and the phone in your pocket. ✅H
- Flowers depend on **distance moved**, not steps or time, up to about 20 km/h. ✅D (the wiki says the exact cap, 16-20 km/h, varies)
- I found **no source** saying the rate differs between app open, screen off, background, squad screen or bird's-eye view. ❓
- Reported problem: some Android players say planting stops with the screen off; setting the app's battery usage to Unrestricted fixed it for one. ❓
- If you stop moving while petals drain, you get push notifications at 3 and 15 minutes. ✅H
- The planting accelerator doubles flowers for 15 minutes and doubles petal use. ✅H

### Standing in one spot: the math
A cell refills every 5 minutes, so you plant one footprint per 5 minutes however many petals you burn. All 🟡C, from the table above.

| Squad | Flowers / 5 min | Petals / 5 min (continuous) | Flowers per petal | Flowers / hour | Petals / hour | Time 300 petals last | Flowers from 300 |
|---|---|---|---|---|---|---|---|
| 1-9 | 2 | 10 | 0.2 | 24 | 120 | 150 min | 60 |
| 10-19 | 6 | 15 | 0.4 | 72 | 180 | 100 min | 120 |
| 20-29 | 12 | 20 | 0.6 | 144 | 240 | 75 min | 180 |
| 30-39 | 20 | 25 | 0.8 | 240 | 300 | 60 min | 240 |
| 40 | 30 | 30 | 1.0 | 360 | 360 | 50 min | 300 |

- **Pulse instead:** start, stop, wait 5 minutes, repeat. One petal each time plants the whole footprint (30 flowers at squad 40). ✅D That is 12 petals an hour for the same flowers per hour as the table, so about 30x cheaper at 40. 🟡C
- Lag can waste an extra petal if you stop late. ✅W
- Moving fast is far better per petal: one Reddit estimate was about 15 flowers per petal at 40 squad, 4-year-old data. ❓🕰️

### Squad size when you shrink it to feed a subset
- The area and petal rate change only at 10, 20, 30 and 40 Pikmin. 31 plants exactly like 39. ✅W
- **Minimum I'd use: 10.** Under 10 you plant a third of the area for two-thirds of the petals. At 20 and 30 you plant 2x and 3.3x the area of 10 at 1.3x and 1.7x the petals. 🟡C
- Pad your subset with spare Pikmin up to the next multiple of 10 (10, 20, 30). The wiki warns against reducing squad size while planting. ✅W
- Which brackets you can use depends on level: 10 at level 7, 20 at level 9, 30 at level 15, 40 at level 55. ✅W

### Walking without staring at your phone
1. **Fill your squad first** and pick a petal jar with enough: at 40 squad it burns 6 petals a minute, about 360 an hour. 🟡C
2. **Start planting when you set off**; it stops on its own when petals run out. ✅H
3. **Plan loops, not out-and-backs.** Each lap at least 5 minutes long, and avoid roads and waterways, which can't take flowers. ✅H
4. **Let the notifications do the checking.** You'll get one at 3 minutes if you've stalled. ✅H
5. **Big Flowers need no counting:** loop inside the 40 m ring on the map; it blooms at 300 flowers, shared across all players. ✅W
6. **Battery:** set location to "always", leave the screen off, and turn off "With Others". ❓ (from tech-site tips and the Help Center; battery use is a known weak spot)

### Big Flowers
- **Official name:** "Big Flower". Stages: Sprout (0-49 flowers), Bud (50-299), Blooming (300+). ✅W "Big sprout" and "big bloom" are community terms.
- **Radius** 40 m; stays bloomed 23 hours; planting in the first hour earns a fruit expedition. ✅W ✅D
- **Coins from planting:** 1 per 250 flowers in a single planting, up to 60 a day. ✅H (this replaces the conflicting 500/30 note.)

#### When to bloom with petals (instabloom)
- **Cost:** 150 petals (unbloomed), 80 (already bloomed, postcard only). ✅D
- **Not worth it for nectar.** Planting is far cheaper: a bloom needs 300 flowers, which is about 10 pulse-petals at squad 40. 🟡W/C
- **Worth it when** your petals would overflow the cap anyway, you want that special postcard, or you need a specific colour fast. 🟡W
- Only the month's primary and secondary species work. ✅D

---

## 9. Social: friends, postcards, party walks

- **Friend cap:** 650 across all Niantic games (since 2026-01-13). ✅D

### What friends are for
| Interaction | Real game value? |
|---|---|
| Mushroom battles: more players raises total attack power and score, so better rewards; invite via bullhorn | **Yes** ✅D |
| Weekly challenge groups: planting reward is 1 petal per 1,000 flowers planted per player in the group | **Yes** ✅D |
| Invite code: a new player who enters yours gets 20 petals + 10 nectar; you can earn up to 4 invite rewards a month | Small 🟡W |
| Postcards | None for gameplay ✅D |
| Gift Bundles from the shop | Gift only 🟡W |
| Party walks | Keepsake only (see below) 🟡W |
| Friendship badges: Apprentice (1), Novice (200), Enthusiast (800), Expert (1,600), Master (3,200) interactions | Badge only 🟡W |

### Postcards
- **Point:** none for gameplay; they're a collectible and a gift. ✅D
- **Sending:** the Pikmin and postcard travel 12 hours, whatever the distance. ✅D✅W
- **Return:** the Pikmin returns right after your friend receives it; if the friend is inactive, 2 days. ✅D (the wiki says 3 days; Discord is newer.)
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

- [x] Release gives plain-colour petals: wiki says so, matches lizz's observation (§1)
- [ ] Rare decor: points per category, Huge seedling 200 vs 230, gold seedlings, level carry-over (§3)
- [ ] Seedling unlock levels: overview.md has two conflicting tables (L259-262 vs L1363-1367)
- [ ] Mushroom unlock level: 9, 12, or 15?
- [ ] Planting footprint axis and whether it's centred on you (§8)
- [ ] Does the planting rate differ with screen off, background, or other screens? (§8)
- [ ] Normal and giant mushroom reward rows (§7)
- [ ] Real total of decor Pikmin (§1)
- [ ] Do step slots share steps across seedlings or split them?
- [ ] Do Party Walk steps do anything beyond the Memento Card? (§9)
- [ ] Is the 3 am mushroom reset in effect now (the FAQ says "from Oct 5")?

## Provenance
Discord #faq copied 2026-11-01. Reddit threads referenced in overview.md could not be fetched, so R-tagged items come only from the notes already pasted there.
