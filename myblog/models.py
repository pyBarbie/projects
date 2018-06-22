from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(max_length=500, help_text='Information about Client  ')

    LOAN_STATUS = (
        ('b', 'Blogger'),
        ('s', 'Simple User'),

    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='s', help_text='status of user')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):

        return reverse('blogger-detail', args=[str(self.id)])



class Post(models.Model):
    title = models.CharField(max_length=100, null=True )
    blogger = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)
    text = models.TextField(max_length=1000, help_text='Text of post, max length 1000 chars ')

    def __str__(self):
        return '{} ({})'.format(self.title, self.pub_date)

    def get_absolute_url(self):

        return reverse('blog-id', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=400, help_text='Text of comment')
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.text)

    # def get_absolute_url(self):
    #     pass
