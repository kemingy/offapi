import json
import os

import httpx  # type: ignore

with open(os.path.join("offapi", "url.json")) as f:
    urls = json.load(f)

def download_files(url, path):
    with httpx.stream("GET", url) as response, open(path, "wb") as f:
        for chunk in response.iter_bytes():
            f.write(chunk)


def pdm_build_initialize(context):
    context.ensure_build_dir()
    os.makedirs(os.path.join(context.build_dir, "offapi"), exist_ok=True)
    for key, url in urls.items():
        download_files(url, os.path.join(context.build_dir, "offapi", key))
