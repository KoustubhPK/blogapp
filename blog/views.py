from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import VipPost, Post, ContactUs

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )

# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['vippost'] = VipPost.objects.all().order_by('-date_posted')
        
        context['tranding_post'] = Post.objects.order_by('-date_posted')[0:3]
        context['tranding_vippost'] = VipPost.objects.order_by('-date_posted')[0:3]

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class VipPostDetailView(DetailView):
    model = VipPost
    template_name = 'blog/vip_post_detail.html'

class TrandingVipPostDetailView(DetailView):
    model = VipPost
    template_name = 'blog/tranding_vip_post_detail.html'

class TrandingPostDetailView(DetailView):
    model = Post
    template_name = 'blog/tranding_post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/userlogin/'
    redirect_field_name = 'userlogin'   
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['category', 'image', 'title', 'description', 'content']

    def form_valid(self, form):
        form.instance.author =  self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/userlogin/'
    redirect_field_name = 'userlogin'
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['category', 'image', 'title', 'description', 'content']

    def form_valid(self, form):
        form.instance.author =  self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/userlogin/'
    redirect_field_name = 'userlogin' 

    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchView(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'all_search_results'


    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Post.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result

def about(request):
    return render(request, 'blog/about.html')

def PageNotFound(request):
    return render(request, 'error/pagenotfound.html')

def contact(request):
    if request.method == "POST":    
        contact = ContactUs()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        messages.success(request, f"Thank you {name}, Your messange is submitted successfully! We'll get back to you soon.")           
        return redirect('contact')
    return render(request, 'blog/contact.html')


def mahabharata(request):
    return render(request, 'blog/mahabharata_war.html')

def karna(request):
    return render(request, 'blog/karna_war.html')

def military(request):
    return render(request, 'blog/role-of-military.html')

def shiva(request):
    return render(request, 'blog/shivaji-maharaj-warfare.html')