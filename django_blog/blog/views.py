from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth.models import User
from .models import *

from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,
                  'blog/homepage.html',
                  {})


class ListUserView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'blog/user_list.html'


@login_required
def post_list(request, id):
    user = get_object_or_404(User, pk=id)
    posts = user.blog_posts.all().filter(status='published')
    return render(request,
                  'blog/post_list.html',
                  {'posts': posts})


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail_post.html'


from .forms import *
import datetime

@login_required
def create_post(request):
    user = request.user

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.created = datetime.datetime.now()
            post.updated = datetime.datetime.now()
            post.save()
            return HttpResponseRedirect(reverse('user-detail', args={user.id}))

        return HttpResponseRedirect(reverse('home'))

    else:
        form = PostForm()

    return render(request,
                  'blog/create_post.html',
                  {'form': form})

@login_required
def update_post(request, pk):
    error_message = ''
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if post.author == user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            post = form.save(commit=False)
            post.updated = datetime.datetime.now()
            post.save()

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user-detail', args={user.id}))

            error_message = 'что-то пошло не так'
            return HttpResponseRedirect(render(request,
                                               'blog/error_page.html',
                                               {'message':error_message}))

        else:
            form = PostForm(instance=post)

        return render(request,
                      'blog/create_post.html',
                      {'form': form})
    else :
        error_message = 'вы не можете редактировать данный пост '
        return render (request,
                       'blog/error_page.html',
                       {'message':error_message})