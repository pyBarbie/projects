from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Client, Post, Comment

# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

from django.views import generic
class BloggerListView(generic.ListView):
    model = Client

    def get_queryset(self):

        return Client.objects.filter(status = 'b')


class BloggerDetailView(generic.DetailView):
    model = Client

class BlogDetailView(generic.DetailView):
    model = Post

class BlogListView(generic.ListView):
    model = Post

from django.http import HttpResponseRedirect
from .forms import CreateCommentForm
from django.urls import reverse
import datetime
from django.urls import reverse_lazy


class CommentCreate(CreateView):
    template_name = 'myblog/create_new_comment.html'
    model = Comment
    fields = ('text',)


    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context


    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        client = self.request.user.client_set.all()[0]
        form.instance.user = client
        form.instance.pub_date = datetime.datetime.now()
        # Associate comment with blog based on passed id
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-id', kwargs={'pk': self.kwargs['pk'],})

# def create_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = CreateCommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment()
#             comment.post = post
#             comment.pub_date = datetime.datetime.now()
#             comment.text = form.cleaned_data['comment']
#             comment.user = post.blogger
#             comment.save()
#             return HttpResponseRedirect(reverse('blog-id',args=[pk]))
#     else:
#         form = CreateCommentForm()
#
#     return render(request, 'myblog/create_new_comment.html', {'form':form} )
