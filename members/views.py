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


# Create your views here.
def my_collection(request):
    shoe_count = 1
    while (shoe_count <= 100):
            # if shoe_count:
            if (shoe_count == 1):
                messages.success(request, ('NICE COLLECTION!'))
                print(str(shoe_count) + '. Nice Collection!')
            
            elif (shoe_count == 10):
                messages.success(request, ('COOL COLLECTION!'))
                print(str(shoe_count) + '. Cool Collection!')
                
            elif (shoe_count == 25):
                messages.success(request, ('DOPE COLLECTION!'))
                print(str(shoe_count) + '. Dope Collection!')

            elif (shoe_count == 50):
                messages.success(request, ('SUPREME CLIENTELE!'))
                print(str(shoe_count) + '. Supreme Clientele!')

            elif (shoe_count == 80):
                messages.success(request, ("SHOELLIONAIRE STATUS!"))
                print(str(shoe_count) + '. Shoelionaire Satus!')

            else:
                print(str(shoe_count) + '.') 
            shoe_count+=1
    else:
        print('This message is outside the loop!')

    if request.user.is_authenticated:
        me = request.user.id
        posts = Post.objects.filter(author=me)
        shoe_count = Post.objects.filter(author=me).count() 

        return render(request, 'registration/my_collection.html', {
        'posts':posts,
        'shoe_count':shoe_count
        })
    
    else:
        # messages.success(request, ('You gotta Login!'))
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