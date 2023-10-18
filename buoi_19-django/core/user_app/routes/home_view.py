from django.views import View
from django.shortcuts import HttpResponse


import requests
import json


data_json = None

class HomeView(View):
    
    def get(self):
        global data_json

        get_data = requests.get("https://jsonplaceholder.typicode.com/posts")
        data_json = json.loads(get_data.text)
        html =""
        button = f'''
            <a href="http://127.0.0.1:8000/filter/?action=10">Filter</a>
            '''
        html += button
        # print(self)
        # if self.request.GET.get("action"):
        #     data_json = data_json[:10]

        for item in data_json:
            print(item)
            html += f'''
                    <div>
                        <h3>{item["id"]}. {item["title"]}</h3>
                        <p>{item["body"]}</p>
                    </div>
                    '''
        return HttpResponse(html)
    

def filter_data(request):
    global data_json

    if request.GET.get("action"):
        data_json = data_json[:int(request.GET.get("action"))]
        html =""
        button = f'''
            <a href="http://127.0.0.1:8000/filter/?action=10">Filter</a>
            '''
        html += button
        # if self.request.GET.get("action"):
        #     data_json = data_json[:10]

        for item in data_json:
            print(item)
            html += f'''
                    <div>
                        <h3>{item["id"]}. {item["title"]}</h3>
                        <p>{item["body"]}</p>
                    </div>
                    '''
        return HttpResponse(html)