from django.db import models

class Count(models.Model):
    hello_text = models.CharField(max_length=200)
    times = models.IntegerField(default=0)
    def __str__(self):
        return self.hello_text