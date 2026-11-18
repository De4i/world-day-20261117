# world-day-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/De4i/world-day-20261117/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/De4i/world-day-20261117/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**The world's news in one picture, for Wednesday 18 November 2026** — one 1024×1024 dashboard of the day:
45 numbered stories from six continents, twelve illustrated modules, a world map carrying a pin for every
story that happened in a place, roughly thirty more one-line briefs, and the day in numbers.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program writes `out/entry.png` — the picture it ships, byte for byte, with no dependencies and no network.

## What is in here

- `main.ts` — the entrypoint: publishes `entry.png` to the output directory (Node 22, standard library only).
- `entry.png` — the entry itself: 18 November 2026 as one picture, 1024×1024, under 1 MiB.
- `poster/poster-v5.html` — the page the entry was rendered from: the day's stories, its layout, its
  drawn illustrations and the world map. `poster/poster-v4.html` and `poster/poster-v3.html` are the
  newspaper-style pages the previous day's entries were built from.
- `poster/BUILD.md` — how each PNG was rendered, and what the day's sources were.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
