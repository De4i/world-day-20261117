# world-day-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/De4i/world-day-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/De4i/world-day-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

**The World Day** — one 1024×1024 front page summing up Tuesday 17 November 2026's world news: 50 stories from six continents, 11 editorial illustrations, a world map of the 12 places the day turned on, and the day in numbers.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program writes `out/entry.png` — the front page it ships, byte for byte, with no
dependencies and no network.

## What is in here

- `main.ts` — the entrypoint: publishes `entry.png` to the output directory (Node 22, standard library only).
- `entry.png` — the entry itself: the day's news as one picture, 1024×1024, under 1 MiB.
- `poster/poster.html` — the page the entry was rendered from: the day's stories, its
  layout, its editorial illustrations in SVG, and the world map.
- `poster/BUILD.md` — how the PNG was rendered from the page, and the day's sources.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
