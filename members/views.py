from asyncore import loop
from atexit import register
from msilib.schema import ListView
from pydoc import pager
from unicodedata import category
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy  # Reverse lazy will redirect back
from .forms import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from ShoeN.models import Profile, Post 
from django.contrib.auth.models import User
from django.contrib import messages
# Import Pagination Here
from django.core.paginator import Paginator

# Create your views here.
def my_collection(request):
    if request.user.is_authenticated:
        me = request.user.id
        posts = Post.objects.filter(author=me).order_by('category')
        shoe_count = Post.objects.filter(author=me).count() 

# Collection counter
        if(shoe_count == 3):
            messages.success(request, ('NICE COLLECTION!'))
            print('Nice Collection')
        elif(shoe_count == 15):
            messages.success(request, ('COOL COLLECTION!'))
            print('Cool Collection')
        elif(shoe_count == 100):
            messages.success(request, ('DOPE COLLECTION!'))
            print('Dope Collection')
        elif(shoe_count == 500):
            messages.success(request, ('SUPREME CLIENTELE!'))
            print('Supreme Clientele')
        elif(shoe_count == 2755):
            messages.success(request, ("SHOELLIONAIRE STATUS!"))
            print('Shoellionaire Status')

        # Pagination setup 
        p = Paginator(Post.objects.filter(author=me).order_by('category'),25 )
        page = request.GET.get('page')
        posts_list = p.get_page(page)
        nums = "a" * posts_list.paginator.num_pages

        return render(request, 'registration/my_collection.html', 
        {'posts':posts,
        'shoe_count':shoe_count,
        'posts_list':posts_list,
        'nums':nums}
        )

    else:
        # You cannot view My Collection from Arclticle details.html unless logged in.
        return redirect('home')

# Show Profile is not in use, runs on backend
class ShowProfilePageView(ListView):
    model = Post
    template_name = 'registration/user_profile.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        page_user = Post.objects.filter(id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        # page_user = get_object_or_404(Post, id=self.kwargs['pk'])

        context['page_user'] = page_user        
        return context

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'instagram_url', 'twitter_url', 'meta_url', 'pinterest_url', 'soundcloud_url', 'snapchat_url', 'youtube_url'] 
    success_url = reverse_lazy('home')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user