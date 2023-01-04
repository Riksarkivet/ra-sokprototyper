# TORA Thor configuration

This folder contains TORA/Riksarkivet-specific configuration for the Thor SPARQL editor and visualization interface.

## Setup

```bash
git clone https://github.com/Abbe98/thor.git
cd thor/config
wget https://github.com/Abbe98/ra-sokprototyper/blob/main/thor/config.rq
```

Follwoing this, you should be able to run any static web server in the `thor` folder.

### Setup query library (optional)

The Thor configuration is set to look for a query library in `config/queries.json`. An example of how individual SPARQL files can be compiled into a library can be seen [here](https://github.com/fornpunkt/sparql/blob/main/query-library/generate_query_lib.py). An example library can be seen [here](https://github.com/fornpunkt/sparql/blob/main/editor/queries.json).
