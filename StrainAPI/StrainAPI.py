import requests

class strainer():

    def __init__(self, key):
        self.key = key

    def get_strain(self, search_type, query):
        url='http://strainapi.evanbusse.com/{}/strains/search/'.format(self.key)
        if(search_type == 'All'):
            url = url+'all'
        elif(search_type == 'name'):
            url = url+'name/{}'.format(query)
        elif(search_type == 'race'):
            url = url+'race/{}'.format(query)
        elif(search_type == 'effect'):
            url = url+'effect/{}'.format(query)
        elif(search_type == 'flavor'):
            url = url+'flavor/{}'.format(query)

        print(url)
        return requests.request("GET", url)