import csv
import shutil
import os

import requests

items = list()
with open('queryResults.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
    next(reader, None)
    items = list(reader)

for item in items:
    image_id = item[7].strip()
    filepath = f'images/{image_id}.jpg'
    if os.path.isfile(filepath):
        continue

    url = f'https://lbiiif.riksarkivet.se/arkis!{image_id}/full/max/0/default.jpg'
    # download stream image
    print(f'Downloading {url} to {filepath}')
    # streaming and copying file object to save memory
    r = requests.get(url, timeout=None, stream=True)

    with open(filepath, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
