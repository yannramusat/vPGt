# Transforming Property Graphs

## About project

## Prerequisites

### iBench

We made iBench an optional dependency by providing the input data for each scenario under `output-ibench-data`.
You can install **iBench** from our [fork](https://github.com/nodejs/node](https://github.com/yannramusat/ibench). (We patched the build process.)

### Neo4j Installation & Configuration

We are connecting to a local Neo4j Community Edition instance to perform the experiments. 

This instance should be configured with the default settings commonly found in `$NEO4J_CONF/neo4j.conf`; 
but to access CSV files located anywhere in the local filesystem, we need to make sure that Neo4j is additionally configured this way:
```
#server.directories.import=import
dbms.security.auth_enabled=false
#dbms.security.allow_csv_import_from_file_urls=true
```

Hence, no credentials are needed and we can freely use `LOAD CSV` to import the data generated by iBench into Neo4j.

Start the server by typing: `sudo /opt/neo4j/bin/neo4j start`.\
*Note:* Do this instead of `sudo -u neo4j /opt/neo4j/bin/neo4j start` to avoid permission errors when loading files.

This software is configured to connect to `localhost` with the default port and with no authentication.

## Installation & Run experiments

### Using venv

```
git clone git@github.com:yannramusat/vPGt.git
cd vPGt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
...
deactivate
```

## Specs

We are running the experiments on the following system: 
* HP EliteBook 840 G3 (L3C67AV)
* Intel(R) Core(TM) i7-6600U CPU @ 2.60GHz
* 32GiB system memory (2133 MHz)

And we are using the following toolchain:
* java-openJDK-17
* Neo4j Community Edition 5.9.0
* Neo4j Python Driver 5.9.0

## Folder Structure
    .
    ├── figures                 # Source code for figure generation
    ├── input-ibench-config     # Configuration files for iBench
    ├── output-ibench-data      # CSV data
    ├── scenarios               # Cypher scripts per scenarios
    └── ...




