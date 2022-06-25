from msilib.schema import ListView
from pydoc import pager
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy  # Reverse lazy will redirect back
from .forms import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from ShoeN.models import Profile, Post 

# Create your views here.

class ShowProfilePageView(ListView):
    model = Post
    template_name = 'registration/user_profile.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        page_user = Post.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        # page_user = get_object_or_404(Post, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

# def show_profile_page(request):
#     cat_menu_list = Post.objects.all()
#     return render(request, 'registration/user_profile.html', {'cat_menu_list': cat_menu_list})

    # def show_profile_page(request):
    #     event_list = Post.objects.all()
    #     return render(request, 'registration/user_profile.html', 
    #     {'event_list': event_list})

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