# The YAP Python API Wrapper

## Installation
    pip install yap-api


## Basic usage
First you need to make sure you have a running YAP Parser Server. The default server installation listens on localhost:8000.

```
from yap_api import YapClient


client = YapClient('http://localhost:8000')
result = client.joint("גנן גידל דגן בגן")
```

## Parsing Responses
Each response will be an object containing the raw response, and list of dictionaries, each dictionary will contain the values of each table line

#### Joint response:
* raw - contains the original response from yap-api
* dep_tree: list of DependencyEntry object
* ma_lattice: list of MorphAnalysisEntry
* md_lattice: list of MorphAnalysisEntry


#### MaResponse
* raw - contains the original response from yap-api
* ma_lattice - list of MorphAnalysisEntry, each raw in original response become MorphAnalysisEntry object

#### MdResponse
* raw - contains the original response from yap-api
* md_lattice - list of MorphAnalysisEntry, each raw in original response become MorphAnalysisEntry object

#### DepResponse
* raw - contains the original response from yap-api
* dep_tree - list of DependencyEntry, each raw in original response become DependencyEntry object

### MorphAnalysisEntry - for ma and md 

* morpheme_start
* morpheme_end
* form 
* lemma
* cpos
* fpos
* eatures
* space_delimited


### DependencyEntry

* morpheme_index
* form 
* lemma
* cpos
* fpos
* features
* dep_head
* dep_label






