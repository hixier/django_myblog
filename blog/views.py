from django.shortcuts import render
from .models import Author, Blog, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateCommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime
# Create your views here.


def index(request):
    """
    View function for home page of site
    :param request:
    :return:
    """
    # create counts of objects
    num_blogs = Blog.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={'num_blogs':num_blogs})


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context


class BlogDetailView(generic.DetailView):
    model = Blog


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required()
def comment_create(request, pk):
    blog_inst = get_object_or_404(Blog, pk=pk)

    # if this is a POST request then process the Form data
    if request.method == 'POST':

        # create a form comment and populate it with data from the request
        form = CreateCommentForm(request.POST)

        # check it if the form is valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

            return HttpResponseRedirect(reverse('blog-detail-view', args=[pk]))
    else:
        form = CreateCommentForm(initial={'comment_text': 'Loin to comment'})

    return render(request, 'blog/comment_form.html', {'form': form, })



    





