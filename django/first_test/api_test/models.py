from django.db import models

class Topic(models.Model):
    topic_title = models.CharField(max_length=200)
    topic_detail = models.CharField(max_length=200)
    topic_time = models.BigIntegerField(default=0)