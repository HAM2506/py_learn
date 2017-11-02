from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json
from .models import Count

# Create your views here.
count = Count.objects.get(pk=1)

def get_hello(request):
    count.times += 1
    if count.times == 16: 
        count.times = 1
    count.save()
    hello_info = {
        'resCode': 'Success', 
        'data': {
            'text': count.hello_text, 'times': count.times, 
        }
    }
    return HttpResponse(json.dumps(hello_info))

    
def get_helloCount(request):
    hello_info = {
        'resCode': 'Success', 
        'data': {
            'text': count.hello_text, 'times': count.times, 
        }
    }
    if 'text' in request.GET:        
        text = request.GET['text'] 
        Count.objects.get(hello_text = text)
    else:
        hello_info['resCode'] = 'Fail'
    return HttpResponse(json.dumps(hello_info)) 