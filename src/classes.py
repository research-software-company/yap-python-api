import requests

class YapResponse:
    def __init__(self, response_content): # instance variable unique to each instance
        self.raw_response = response_content

class MorphAnalysisEntry:  # for ma and md requests
    def __init__(self, tsv_line:'string'): # instance variable unique to each instance
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
    def __init__(self, tsv_line:'string'): # instance variable unique to each instance
        splitted =  tsv_line.split('\t')
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
        splitted = response['ma_lattice'].split('\n')
        ma_response = []
        for row in splitted:
            if not row =='':
                ma_entry = MorphAnalysisEntry(row)
                ma_response.append(ma_entry)
        self.ma_lattice = ma_response

class MdResponse(YapResponse):
    def __init__(self, response):
        super().__init__(response)
        splitted = response['md_lattice'].split('\n')
        md_response = []
        for row in splitted:
            if not row =='':
                md_entry = MorphAnalysisEntry(row)
                md_response.append(md_entry)
        self.md_lattice = md_response


class DepResponse(YapResponse):
    def __init__(self, response):
        super().__init__(response)
        splitted = response['dep_tree'].split('\n')
        dep_response = []
        for row in splitted:
            if not row =='':
                dep_entry = DependencyEntry(row)
                dep_response.append(dep_entry)
        self.dep_tree = dep_response
 
class JointResponse(MaResponse, MdResponse, DepResponse):
    pass

class Client():
    def __init__(self, url="http://localhost:8000"):
        self.api_url = url

    def ma(self, text: 'string'):
        textBody = '{"text": "' + text +'  "}'
        response = self.send_request(textBody, 'ma')
        result = MaResponse(response)
        return result

    def md(self, ma: 'MaResponse'):
        textBody = '{"ambLattice": "' + ma.raw_response['ma_lattice'] +'  "}'
        response = self.send_request(textBody, 'md')
        result = MdResponse(response)
        return result

    def dep(self, md: 'MdResponse'):
        textBody = '{"disambLattice": "' + md.raw_response['md_lattice'] +'  "}'
        response = self.send_request(textBody, 'dep')
        result = DepResponse(response)
        return result

    def joint(self, text: 'string'):
        textBody = '{"text": "' + text +'  "}'
        response = self.send_request(textBody, 'joint')
        result = JointResponse(response)
        return result

    def send_request(self, textBody: 'string', url_endpoint: 'string'):
        _base_url = self.api_url +"/yap/heb/"
        headers = {'Content-type': 'application/json'}
        body = textBody.encode('utf-8')
        response = requests.get(_base_url+url_endpoint, headers=headers, data=body)
        return response.json()


# if __name__ == '__main__':
#     client = Client()
#     joint = client.joint("גנן גידל דגן בגן")
#     ma = client.ma("גנן גידל דגן בגן")
#     md = client.md(ma)
#     dep = client.dep(md)


    