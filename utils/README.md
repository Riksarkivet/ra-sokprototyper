# Various utilities for working with National Archives data

## `RA RDF Downloader.ipynb`

Jupyter notebook interface for traversing and downloading all IIIF resources that are childs of a given collection.

## `expand_jsonld.sh`

Bash script for exapnding all JSONLD files in a given folder. Requries [jsonld-cli](https://github.com/digitalbazaar/jsonld-cli).

## `prefixes.rq`

SPARQL formatted RDF prefixes for IIIF resources.

## `list_metadata_given_a_manifest.rq`

Basic SPARQL query for listing IIIF metadata entries for a given manifest.

## `graph_to_canvas_table.rq`

SPARQL query that parses IIIF metadata and outputs a canvas level table.

## `iiif-image-index-builder.py`

Python script for building the image index needed for displaying images in grid-browser's "browse" mode.
