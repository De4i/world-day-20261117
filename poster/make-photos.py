#!/usr/bin/env python3
"""Make the front page's photographs.

Cloudflare Workers AI serves FLUX.1-schnell, which is what these calls use
(CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID in the environment). Each
prompt asks for a documentary news photograph and, deliberately, for no text
and no lettering: image models draw lettering badly, and a front page is
spelled out by its own type, never by the picture.

Run it from this directory to regenerate `img/`. The page itself ships the
rendered crops, so nothing here is needed to build the entry.
"""
import base64
import json
import os
import urllib.request

from PIL import Image

TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
ACCOUNT = os.environ["CLOUDFLARE_ACCOUNT_ID"]
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-1-schnell"

TRAILER = ", documentary news photograph, no text, no lettering, no logos"

SHOTS = {
    "plenary": "wide photograph of an international summit plenary hall seen from the press gallery, rows of delegates at long desks, interpreter booths, big screens above the stage, warm indoor light",
    "bridge": "long road-and-rail bridge across a wide strait at dawn, black smoke rising from its central span, low mist on the water",
    "markets2": "dealing room in low light, rows of monitors with blurred price charts, backs and hands of traders, shallow depth of field",
    "climate": "climate summit conference hall seen from the floor, delegates seated at desks, large glowing globe on a screen, warm indoor light",
    "ebola": "health workers in white protective suits outside a treatment centre in central Africa, grey tents, red dusty ground",
    "court": "courthouse building in an African capital, police cordon and waiting journalists outside, hot hazy daylight",
    "cyclone": "enormous storm clouds over a tropical coastline, fishing boats hauled ashore, monsoon light, wet sand",
    "floods": "flooded township street with corrugated-iron houses, brown water running between them, overcast sky",
    "cricket2": "evening floodlit cricket match, batsman at the crease seen from behind the bowler, green pitch, packed stands",
    "clinic": "measles vaccination clinic in a school gymnasium, nurse with syringe and a child, parents waiting in line, soft daylight",
}

# name in SHOTS -> (crop width, crop height, where to keep the crop vertically,
#                   file the page loads)
CROPS = {
    "plenary": (690, 152, 0.42, "hero-summit.jpg"),
    "bridge": (288, 74, 0.45, "kerch.jpg"),
    "markets2": (288, 74, 0.45, "markets.jpg"),
    "climate": (236, 68, 0.42, "climate.jpg"),
    "cyclone": (236, 68, 0.42, "cyclone.jpg"),
    "court": (236, 68, 0.42, "court.jpg"),
    "ebola": (236, 68, 0.42, "ebola.jpg"),
    "floods": (236, 68, 0.42, "floods.jpg"),
    "cricket2": (236, 68, 0.42, "cricket.jpg"),
    "clinic": (236, 68, 0.42, "clinic.jpg"),
}


def generate(name: str, prompt: str, out_dir: str) -> str:
    body = json.dumps({"prompt": prompt + TRAILER, "steps": 4}).encode()
    request = urllib.request.Request(
        URL, data=body,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    answer = json.loads(urllib.request.urlopen(request, timeout=180).read())
    path = os.path.join(out_dir, name + ".jpg")
    with open(path, "wb") as handle:
        handle.write(base64.b64decode(answer["result"]["image"]))
    return path


def crop_to(page: Image.Image, width: int, height: int, focus: float) -> Image.Image:
    """Centre-crop to the frame the page gives the picture, then scale to it."""
    wide, tall = page.size
    ratio = width / height
    if wide / tall > ratio:
        keep = int(tall * ratio)
        left = (wide - keep) // 2
        page = page.crop((left, 0, left + keep, tall))
    else:
        keep = int(wide / ratio)
        top = int((tall - keep) * focus)
        page = page.crop((0, top, wide, top + keep))
    return page.resize((width, height), Image.LANCZOS)


def main() -> None:
    raw = os.path.join(os.path.dirname(__file__), "raw")
    img = os.path.join(os.path.dirname(__file__), "img")
    os.makedirs(raw, exist_ok=True)
    os.makedirs(img, exist_ok=True)
    for name, prompt in SHOTS.items():
        path = generate(name, prompt, raw)
        width, height, focus, target = CROPS[name]
        with Image.open(path) as page:
            crop_to(page.convert("RGB"), width, height, focus).save(
                os.path.join(img, target), quality=88, optimize=True
            )
        print(f"{name} -> img/{target}")


if __name__ == "__main__":
    main()
