# The YAP Python API Wrapper

## Installation
    pip install yap-api


## Basic usage
First you need to make sure you have a running YAP Parser Server. The default server installation listens on localhost:8000.

```
from yap_api import YapClient


client = YapClient('localhost:8000')
result = client.joint("גנן גידל דגן בגן")
```

## Parsing Responses
Two sentences describg the results (the raw result and the list of objects)

Explain JointResponse

Explain other responses

### MorphAnalysisEntry - for ma and md 
fields:

morpheme_start
morpheme_end
form 
lemma
cpos
fpos
eatures
space_delimited

### MaResponse
raw_response - contains the original response from yap-api
ma_lattice - list of MorphAnalysisEntry, each raw in original response become MorphAnalysisEntry object



### MdResponse
raw_response - contains the original response from yap-api
md_lattice - list of MorphAnalysisEntry, each raw in original response become MorphAnalysisEntry object

### DependencyEntry
fields:

morpheme_index
form 
lemma
cpos
fpos
features
dep_head
dep_label

### DepResponse

raw_response - contains the original response from yap-api
dep_tree - list of DependencyEntry, each raw in original response become DependencyEntry object

### JointResponse

raw_response - contains the original response from yap-api
dep_tree: DepResponse
ma_lattice: MorphAnalysisEntry
md_lattice: MorphAnalysisEntry

