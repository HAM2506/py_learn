from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse

import json
from .models import Topic

# Create your views here.

def get_topic(request):
    topic = Topic.objects.all()
    topicList = serializers.serialize('json', Topic.objects.all())
    parseTopic = []
    for i in json.loads(topicList):
        parseTopic.append(i['fields'])
    topic_info = {
        'resCode': 'Success', 
        'data': parseTopic
    }
    return HttpResponse(json.dumps(topic_info))

def save_topic(request):
    print(request.GET.get('title'))
    title = request.GET.get('title').encode("utf-8")
    detail = request.GET.get('detail').encode("utf-8")
    time = request.GET.get('time')
    topic = Topic(topic_title=title, topic_detail=detail, topic_time=time)
    topic.save();
    save_info = {
        'resCode': 'Success'
    }
    return HttpResponse(json.dumps(save_info))