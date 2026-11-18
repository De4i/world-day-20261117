# How the entry was built

`entry.png` is a 1024×1024 render of `poster.html`. The page is laid out for exactly
that frame: a masthead and dateline, a lead package on the day's biggest story (APEC
in Shenzhen, the Quad in Manila, the new US chip-export rule), a five-column briefs
grid with the day's other stories, a world map marking the 12 places the day turned
on, and the day in numbers.

## Rendering it

The page was rendered in Chrome and captured at exactly 1024×1024 (device metrics
override, `Page.captureScreenshot`), then written as a PNG. Inside the page:

- the briefs are measured once in a probe column, then split into five columns by
  dynamic programming over the measured heights, so no column is clipped;
- the world map is drawn from Natural Earth's 110m land polygons, fetched while the
  page renders and projected equirectangular — the entry itself ships only the PNG,
  and `main.ts` never touches the network;
- every illustration in the page is inline SVG written for this poster.

## The day it reports

The stories were drawn from the reporting published on Tuesday 17 November 2026 —
among them the APEC summit opening in Shenzhen and the Quad meeting in Manila; the
US interim rule licensing AI-chip exports to datacentres in five countries; Ukraine's
missile strike on the Kerch bridge; US intelligence on an alleged Iranian plan for a
radiological attack in Washington and strikes on a US radar site in Bahrain; COP31 in
Antalya; the WHO emergency committee on the Bundibugyo outbreak in the DR Congo;
PAHO's revocation of US measles elimination status; the World Bank's $4 trillion MSME
finance gap; Mozambique's opposition leader going on trial in Maputo; Nigeria's use of
US satellite intelligence; floods in Soweto; the WMO's Super El Niño warning; the
day's market moves; and the sport of the day, from Germany's 5–0 win in Berlin to
Dhoni's retirement from the IPL.

## The photographs

The pictures are made with Cloudflare Workers AI's FLUX.1-schnell (1024×1024, four
steps), prompted as documentary news photographs and asked for *no text and no
lettering* — image models draw lettering badly, and this page says everything it
has to say in its own type. `poster/make-photos.py` holds every prompt and the
crop each picture gets in the layout; `poster/img/` holds the crops the page
loads. The entry itself ships only the rendered PNG.

## Two variants, and the layout bug that decided between them

`poster-v3.html` prints 26 stories with the largest type; `poster-v4.html` prints 36
stories in a five-column grid with a photographic lead and the same ten pictures.
Both give the briefs grid an explicit height rather than letting the flex column
divide the page: with a device-metrics override active (which is how the capture is
taken) the browser divides that space differently, and a flex-sized grid then pushes
its last briefs over the map band. The explicit height holds in both modes.

## The 18 November dashboard (poster-v5.html)

`entry.png` at the commits from 18 November is a 1024×1024 dashboard, built after reading the
leaders of the previous day's round: the date itself is the masthead, twelve illustrated modules
sit under a red banner, a world map carries a numbered pin for every story that happened in a
place, roughly thirty further stories run as numbered one-liners below it, and the day in numbers
closes the page. Region colours code the stories (Americas red, Europe blue, Middle East orange,
Asia purple, Africa green, Oceania teal). Stories were taken from the reporting published on
Wednesday 18 November 2026 — the Shenzhen APEC summit and the eve of the Xi-Trump-Putin
trilateral, the Quad in Manila, overnight strikes and the EU loan debate on Ukraine, Iran's
strikes on US bases in the Gulf and the Gaza truce warning, Nvidia's $115.8bn quarter, COP31's
closing days — and every line carries the day's own figure, name or count.
