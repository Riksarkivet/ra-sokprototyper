import requests

found_uris = list()
starting_collection = 'https://lbiiif.riksarkivet.se/collection/riksarkivet'
collections_needing_images = list()
image_index = list()

import json
def traverse(url):
    r = requests.get(url)
    print(url)

    found_uris.append(url)

    if r.status_code != 200:
        return

    try:
        data = r.json()
    except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
        print(r.text)

    for item in data['items']:

        if item['id'] in found_uris:
            continue

        if item['type'] == 'Collection':
            collections_needing_images.append(item['id'])
            traverse(item['id'])
        elif item['type'] == 'Manifest':
            image = get_image_from_manifest(item['id'])
            if image:
                image_index.append([item['id'], image])
                for collection in collections_needing_images:
                    image_index.append([collection, get_image_from_manifest(item['id'])])
            collections_needing_images.clear()


def get_image_from_manifest(manifest_url):
    try :
        manifest = requests.get(manifest_url).json()
    except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
        print(manifest_url)
        return False
    if len(manifest['items']) > 0:
        item = manifest['items'][round(len(manifest['items']) / 2) - 1]
        if item['type'] == 'Canvas':
            return item['id']
    return False

traverse(starting_collection)

import csv

# write image index to csv
with open('image_index.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(image_index)
