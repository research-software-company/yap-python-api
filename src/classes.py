import requests

class YapResponse:
    def __init__(self, response_content): # instance variable unique to each instance
        self.raw_response = response_content

class MorphAnalysisEntry:  # for ma and md requests
    def __init__(self, tsv_line): # instance variable unique to each instance
        splitted = tsv_line.split('\t')
        self.morpheme_start = splitted[0]
        self.morpheme_end = splitted[1]
        self.form = splitted[2]
        self.lemma = splitted[3]
        self.cpos = splitted[4]
        self.fpos = splitted[5]
        self.features = splitted[6]
        self.space_delimited = splitted[7]

class DependencyEntry: # for dep requests
    def __init__(self, tsv_line): # instance variable unique to each instance
        splitted = re.split(r'\t+', tsv_line.rstrip('\t'))
        self.morpheme_index = splitted[0]
        self.form = splitted[1]
        self.lemma = splitted[2]
        self.cpos = splitted[3]
        self.fpos = splitted[4]
        self.features = splitted[5]
        self.dep_head = splitted[6]
        self.dep_label = splitted[7]

class MaResponse(YapResponse):
    def __init__(self, response):
        super().__init__(response)
        splitted = re.split(r'\n+', response['ma_lattice'].rstrip('\n'))
        ma_response = []
        for row in splitted:
            ma_entry = MorphAnalysisEntry(row)
            ma_response.append(ma_entry)
        self.ma_lattice = ma_respones

class MdResponse(YapResponse):
    def __init__(self, response):
        super().__init__(response)
        splitted = re.split(r'\n+', response['md_lattice'].rstrip('\n'))
        md_response = []
        for row in splitted:
            md_entry = MorphAnalysisEntry(row)
            md_respones.append(md_entry)
        self.md_lattice = md_respones


class DepResponse(YapResponse):
    def __init__(self, response):
        super().__init__(response)
        splitted = re.split(r'\n+', response['dep_tree'].rstrip('\n'))
        dep_response = []
        for row in splitted:
            md_entry = MorphAnalysisEntry(row)
            dep_respones.append(md_entry)
        self.dep_tree = dep_respones
 
class JointResponse(MaResponse, MdResponse, DepResponse):
    pass

if __name__ == '__main__':
    headers = {'Content-type': 'application/json'}
    body = '{"text": "גנן גידל דגן בגן  "}'.encode('utf-8')
    response = requests.get('http://localhost:8000/yap/heb/joint', headers=headers, data=body)
    print(response.json())
    jr = JointResponse(response.json())
    l=0
