from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # ListView will list posts, DetailView will show 1 post
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def search_shoes(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        shoes = Post.objects.all(name__contains=searched)

        return render(request,'search_shoes.html',
        {'searched':searched,
        'shoes':shoes})
    else:
        return render(request,'search_shoes.html',
        {})


def index(request):
    return render(request, 'hangman.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu 
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


# Categories (User shoe collection displayed here).
class CategoryView(ListView):   
        model = Post
        template_name = 'categories.html'
        cats = Post.objects.all()
        ordering = ['-post_date']


# def CategoryView(request, cats):
#     category_posts = Post.objects.filter()
#     return render(request, 'categories.html', {'cats': cats, 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        nod = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = nod.total_likes()

        liked = False
        if nod.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu 
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


