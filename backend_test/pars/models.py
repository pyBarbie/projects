from django.db import models
from django.urls import reverse

class UrlModel(models.Model):
    success = models.BooleanField(default=False)
    url = models.URLField(max_length=200, help_text="Input url for parse", default=None)
    title = models.CharField(max_length=200, help_text='title from url', default=None, null=True, blank=True)
    charset = models.CharField(max_length=200, help_text='encode from url', null=True, blank=True)
    time = models.DateTimeField(null=True)
    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('parse-detail', args=[self.id])


class H1_tag(models.Model):
    url = models.ForeignKey(UrlModel, on_delete=models.CASCADE, related_name='h1_tags')
    tag = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.tag
