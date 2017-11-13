from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse
#403
from django.views.decorators.csrf import csrf_exempt,csrf_protect

import json
from .models import Topic

# Create your views here.

def get_topic(request):
    topic = Topic.objects.all()
    topicList = serializers.serialize('json', Topic.objects.all())
    parseTopic = []
    for i in json.loads(topicList):
        i['fields']['id'] = i['pk']
        parseTopic.append(i['fields'])
    topic_info = {
        'resCode': 'Success', 
        'data': parseTopic
    }
    return HttpResponse(json.dumps(topic_info))

@csrf_exempt
def save_topic(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body['title']
        detail = body['detail']
        time = body['time']
    else:
        title = request.GET.get('title').encode("utf-8")
        detail = request.GET.get('detail').encode("utf-8")
        time = request.GET.get('time')
    topic = Topic(topic_title=title, topic_detail=detail, topic_time=time)
    topic.save();
    save_info = {
        'resCode': 'Success'
    }
    return HttpResponse(json.dumps(save_info))

@csrf_exempt
def delete_topic(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
    topic = Topic.objects.get(pk=id)
    topic.delete();
    save_info = {
        'resCode': 'Success'
    }
    return HttpResponse(json.dumps(save_info))