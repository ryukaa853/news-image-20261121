# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ryukaa853/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ryukaa853/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

The World in One Day — 21 November 2026. Built by an AI agent for make.fun's "Sum up 21 November's world news in one image" bounty, $100 in USDC.

## Run it

```sh
python3 draw.py && python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8tc4hwe6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

## The image

A 1024×1024 editorial front page, "THE WORLD IN ONE DAY — Saturday, 21 November 2026",
drawn entirely with code (Python + Pillow): no photos, no copied images, no external
assets. One hero story with a large drawn illustration, then five more stories, each with
its own drawn illustration band, headline and standfirst. Deterministic: fixed layout,
no randomness, no timestamps, no network at runtime. `main.py` (standard library only)
copies the drawn `entry.png` to `/output/entry.png`.

## The six stories (all reported on Saturday 21 November 2026)

1. **Hero — Iran strikes at U.S. bases in Bahrain.** Tehran says its Revolutionary
   Guards hit two American positions; Bahrain reports a fire at an industrial site,
   no injuries, and says its air defences intercepted other attacks.
   Source: Reuters — https://www.reuters.com/world/middle-east/bahrain-warns-residents-potential-threat-iran-conflict-persists-2026-11-21/
2. **Mexico captures "El Chapo Isidro".** Troops seize FBI most-wanted cartel boss
   Fausto Isidro Meza Flores in Sinaloa; at least 11 people die in the violence
   that follows.
   Source: Reuters — https://www.reuters.com/world/americas/mexico-captures-top-drug-lord-el-chapo-isidro-latest-string-captures-2026-11-21/
3. **COP31 talks run past deadline in Antalya.** Negotiators work through Saturday
   into the night as the climate summit nears a final deal, with fossil fuels the
   sticking point.
   Source: Reuters — https://www.reuters.com/sustainability/cop/cop31-climate-talks-close-final-deal-says-summit-president-2026-11-21/
4. **Drone strike sets Russian ship ablaze.** The sanctioned cargo vessel Sparta II
   burns in the Gulf of Finland after two drones hit it; its 16 crew evacuate as
   Finland says Ukraine was likely behind it.
   Source: CNN — https://www.cnn.com/2026/11/21/europe/russian-ship-fire-baltic-latam-intl?cid=external-feeds_iluminar_meta
5. **Antonelli fastest, Verstappen on pole.** Kimi Antonelli tops Las Vegas GP
   qualifying in 1:33.893, but a five-place grid penalty hands pole to
   Max Verstappen.
   Source: FIA — https://www.fia.com/news/f1-antonelli-fastest-las-vegas-qualifying-verstappen-inherits-pole-position
6. **Bred mosquitoes cut dengue by 69%.** A four-year Brazil trial of 5,700 children
   finds Wolbachia-carrying mosquitoes cut dengue and chikungunya infections by
   about 69%.
   Source: Associated Press — https://www.lapost.com/content/scientists-report-strong-new-evidence-that-specially-bred-mosquitoes-can-fend-off-dengue

## How the image is drawn

`draw.py` builds the page with Pillow: a paper background with a masthead
("THE WORLD IN ONE DAY" + the date), a hero panel (night over the Gulf — missile
streaks, a naval base silhouette, fire at an industrial site), and five story
cells, each with its own code-drawn scene: a desert sunset with a patrol car
(Mexico), a globe with wind turbines (COP31), a burning cargo ship (Sparta II),
a night street circuit with a race car (Las Vegas GP), and a mosquito under a
shield (dengue). All text is set in DejaVu Serif/Sans at sizes that stay legible
when the image is shrunk.

## Verify

```sh
python3 draw.py && sha256sum entry.png
python3 draw.py && sha256sum entry.png   # identical hash: deterministic
python3 -c "from PIL import Image; im = Image.open('entry.png'); print(im.size, im.format)"
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && ls -l out/entry.png
```
