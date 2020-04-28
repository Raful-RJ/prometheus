
## Prometheus 

The prometheus analysis framework for ringer and Lorenzett simulator team.

## Dataframe support:

- PhysVal ntuple schemma from athena Online trigger e/g framework;
- SkimmedNtuple schemma from e/g Tag and probe Offline frameworl; 
- Lorenzett from generic simulator;


## Requirements

- root;
- python 3;
- cmake 3;
- Gaugi (pip3 install gaugi).


## Installation:

```bash
# dowload all submodules
source setup_module.sh
# put everything to master
source setup_module.sh --head
# build and compile
mkdir build && cd build && cmake .. && make -j4
```

After the installation, just setup it with:
```bash
# setup the libs and modules
source setup.sh
```


## Contribution:

- Dr. João Victor da Fonseca Pinto, UFRJ/COPPE, CERN/ATLAS (jodafons@cern.ch) [maintainer, developer]
- Dr. Werner Freund, UFRJ/COPPE, CERN/ATLAS (wsfreund@cern.ch) [developer]
- Msc. Micael Veríssimo de Araújo, UFRJ/COPPE, CERN/ATLAS (mverissi@cern.ch) [developer]


