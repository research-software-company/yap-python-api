## Description
python api to activate yap api

### initialize
client = Client(api_url) - default value: 'localhost:8000'

### Endpoints
joint = client.joint(text: string) - gets a string as input and returns JointResponse
ma = client.ma(text:string) - get a string as input returns MaResponse
md = client.md(ma) - gets maResponse object and returns MdResponse
dep = client.dep(md) - gets mdResponse object and retuens DepResponse 

### Classes:

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

