from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserLoginForm, PostForm, PhotoForm, EventForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.service import *

# Create your views here.


def index(request, cnt=8):
    posts = Post.objects.all()
    workphotos = WorkPhotos.objects.all()[:cnt]
    category = CategoryPhoto.objects.all()
    context = {
        'posts': posts,
        'workphotos': workphotos,
        'category': category,
    }

    return render(request, 'blog/index.html', context)


def portfolio(request):
    posts = WorkPhotos.objects.all()
    category = CategoryPhoto.objects.all()
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blog/portfolio.html', context)


'''def blog(request):
    posts = Post.objects.all()
    category = CategoryPost.objects.all()
    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'blog/blog.html', context)
'''
class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 2


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single-blog.html'
    posts = Post.objects.order_by('-views')
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostsByCategory(ListView):
    template_name = 'blog/portfolio.html'
    context_object_name = 'posts'
    paginate_by = 4
    #allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = CategoryPhoto.objects.get(slug=self.kwargs['slug'])
        return context

def adm(request):
    return render(request, 'blog/adm.html')


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('adm')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "blog/add_post.html"
    login_url = "/admin/"
    success_url = reverse_lazy('blog')


class CreatePhoto(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "blog/add_photo.html"
    login_url = "/admin/"
    success_url = reverse_lazy('portfolio')


class PostUpdate(UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    form_class = PostForm


class PhotoUpdate(UpdateView):
    model = WorkPhotos
    template_name = "blog/update_photo.html"
    form_class = PhotoForm
    success_url = reverse_lazy('portfolio')


class PostDelete(DeleteView):
    model = Post
    template_name = "blog/single-blog.html"
    success_url = reverse_lazy('blog')


class PhotoDelete(DeleteView):
    model = WorkPhotos
    template_name = "blog/portfolio.html"
    success_url = reverse_lazy('portfolio')



def add_event(request):
    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #news = News.objects.create(**form.cleaned_data)
            #form.end_time = endTime(form.cleaned_data['start_time'], form.cleaned_data['title'])

            event = form.save(commit=False)
            proc = Procedure.objects.get(name=event.title)
            add_time = datetime.timedelta(proc.time)
            event.end_time = event.start_time + add_time
            event.save()
    else:
        form = EventForm()
    return render(request, 'blog/add_event.html', {'form': form})



def about_us(request):
    return render(request, 'blog/about_us.html')

def services(request):
    return render(request, 'blog/services.html')





'''
class AddEvent(CreateView):
    form_class = EventForm
    template_name = "blog/add_event.html"
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.end_time = endTime(start_time=form.start_time, title=form.title)
        return super(AddEvent, self).form_valid(form)



def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #news = News.objects.create(**form.cleaned_data)
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            post = form.save()
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

'''