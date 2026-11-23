# The World in One Day — Monday, 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/adhiejoey/makefun-news-image-23/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/adhiejoey/makefun-news-image-23/reward.svg)](https://make.fun/bounty/news-image-20261123)

A cream-paper broadsheet that sums up the world's news of **Monday, 23 November 2026** in one
1024×1024 image: a lead story, a labelled schematic world map, a UTC timeline of the day,
and **40 sourced stories** from every continent. Entry for the
[make.fun bounty news-image-20261123](https://make.fun/bounty/news-image-20261123) ($100, 50 places paid).

## The image

`entry.png` (1024×1024, under 1 MiB) is drawn by `draw.py` (Python 3 + Pillow, system DejaVu
fonts) from the verified story list in `stories.py`. `main.ts` (Node 22, standard library only)
copies it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). The program runs with no network
and two runs write byte-identical output.

## Lead story

Russian strike on Dymer flats kills at least 11 — rescuers worked through Monday pulling
survivors from a collapsed five-storey block in Dymer, north of Kyiv, after Russian strikes on
the Kyiv region, as NATO met in Brussels over Russian missiles that crossed into Poland.
(Sources: Reuters, Seven Lights, AP.)

## The 40 stories

Confidence: **HIGH** = two or more sources dated 23 Nov 2026; **MED** = one source dated 23 Nov 2026.

| # | Story | Source | Conf. |
|---|-------|--------|-------|
| 1 | Russian strike on Dymer flats kills at least 11 | Reuters / Seven Lights | HIGH |
| 2 | Ukraine sinks Russian corvette off Libya | AP / China Daily | HIGH |
| 3 | NATO holds emergency council on Poland breach | RMF24 / FBC | HIGH |
| 4 | Russian cargo ship ablaze in the Baltic Sea | France 24 / GEORGE | MED |
| 5 | Kerch Bridge strikes cripple Crimea link | h.ua | MED |
| 6 | Drones set Tatarstan oil station ablaze | h.ua | MED |
| 7 | Drone debris falls on Kyiv school grounds | h.ua / News Media House | HIGH |
| 8 | France PMI falls to 46.2 | Reuters / S&P Global | HIGH |
| 9 | Belgium grinds to a halt in general strike | Demócrata / DPA | HIGH |
| 10 | Thousands march in Brussels on budget cuts | DWS News | MED |
| 11 | Thousands rally in Istanbul for free media | One Turn / GEORGE | HIGH |
| 12 | Netanyahu–Eisenkot talks end with no deal | Arab News | MED |
| 13 | Gaza war left a toxic wasteland, experts say | One Turn | MED |
| 14 | Attacks on West Bank medics up 350% | News Media House | MED |
| 15 | Khartoum drone strikes kill four, hit UN site | Xinhua / One Turn | HIGH |
| 16 | At least 24 civilians killed in South Sudan | One Turn | MED |
| 17 | Ebola toll far above official count | Reuters | HIGH |
| 18 | Houthis claim strike on Saudi refinery | One Turn | MED |
| 19 | Saudi Arabia downs Houthi drone near Riyadh | Al Mayadeen / Arab News | MED |
| 20 | Yemeni army reports 639 strikes on Houthis | Arab News | MED |
| 21 | Bahrain: Iran hit civilian site; tankers struck | France 24 / EventGraph | MED |
| 22 | Trump takes on Newsom over 548 death-row cases | Fox News | MED |
| 23 | Trump moves to curb Congress probes | CNN | MED |
| 24 | $TRUMP coin dinner for top holders | CNN | MED |
| 25 | Foxx concedes; Democrats hold 258 seats | Reuters / AP | MED |
| 26 | Army to blast Iowa explosives despite court | One Turn | MED |
| 27 | Bolsonaro in intensive care in Brasilia | One Turn | MED |
| 28 | S. Korea minister quits over exam chaos | Reuters | HIGH |
| 29 | Asian markets slide on AI bubble fears | Al Jazeera / One Turn | HIGH |
| 30 | Taiwan bans short sales; Asia acts to calm rout | EventGraph / Ainance | HIGH |
| 31 | US futures rebound after Friday's rout | NordFX | MED |
| 32 | Indonesia factory fire: 24 dead, dozens lost | BBC / Reuters | HIGH |
| 33 | Vietnam breaks ground on rare-earth plant | Reuters | HIGH |
| 34 | Bangladesh vows to jail Hasina | Reuters | HIGH |
| 35 | Korea exports top $1 trillion | Yonhap | HIGH |
| 36 | Tata Steel in $1.67bn pipe-maker deal | One Turn | MED |
| 37 | METR: AI outpacing safety testing | The Decoder / EventGraph | HIGH |
| 38 | OpenAI chief floats a shared AI 'ceiling' | OpenAI / EventGraph | MED |
| 39 | Nvidia shows Rubin GPU, due in 2028 | The Daily Gradient | MED |
| 40 | 49ers rout Vikings 35–10 in Mexico City | Reuters | HIGH |

## Date check

Every story above happened, or was first reported, on Monday 23 November 2026. Deliberately
excluded as wrong-date: COP31 collapse (ended Sun 22 Nov) · Alcaraz ATP Finals title (Sun 22 Nov) ·
Márquez 8th MotoGP title (Sun 22 Nov) · Riemann Hypothesis proof certified (21 Nov) ·
Anthropic IPO debut (19 Nov) · Nvidia quarterly results (18 Nov) · Trump Iran / Hormuz remarks
(22 Nov) · Penny law (20 Nov) · El Chapo arrest (20 Nov) · Delta outage (22 Nov) ·
Kh-101 ID (22 Nov) · Killer-robot deal (21 Nov).

## How it was built

1. Researched the day's news on 23 Nov 2026 (Reuters, AP, BBC, Al Jazeera, France 24, CNN, Fox
   News, One Turn and others) and verified every date, number and event against its source.
2. Wrote `stories.py` (40 verified stories + timeline + map points) and `draw.py` (the broadsheet
   renderer) from scratch for this day — no previous day's generator was reused.
3. Rendered `entry.png`, viewed it, and fixed the map labels and text fit.
4. A final date audit re-checked every story against its source and replaced five that
   turned out to be wrong-date (penny law, El Chapo arrest, Delta outage, Kh-101
   confirmation, killer-robot talks) with verified 23 Nov stories, and corrected the
   Dymer death toll from 15 to 11.
5. Ran the make.fun local house check (`makefun check`) until all checks passed, and verified
   determinism by running `main.ts` twice and comparing SHA-256 hashes.

## Reproduce

```sh
python3 draw.py            # rebuild entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copy it to out/entry.png
```

## Licence

MIT — see [LICENSE](LICENSE).
