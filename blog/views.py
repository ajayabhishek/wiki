
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .serializers import ArticleSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



from .models import category
from .models import Article
from .models import Document
from .forms import NameForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




for user in User.objects.all():
    Token.objects.get_or_create(user=user)


def index(request):
    return render(request,'blog/hello.htm',{'data':'whiznet'})

@login_required(login_url='/login/')
def profile_view(request):
    profile = request.user

    data = Article.objects.filter(author= profile).order_by("-created_date")
    context = {'profile': profile, 'data': data}
    template = 'blog/profile.html'
    return render(request, template, context)




def school(request):
    return render(request,'blog/hello.htm',{'data':"school"})

def home(request):
    return render(request,'blog/home.htm', {'data':'You are currently present in the home page !!'})

@login_required(login_url='/login/')
def showform(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        name=''
        if form.is_valid():
            print("OK")
            name1 = form.cleaned_data['cat_id']
            author= request.user
            name3 = form.cleaned_data['title']
            name4 = form.cleaned_data['content']

            Article.objects.create(cat_id=name1,author=author, title=name3, content=name4)

            
            
                    
        return render(request,'blog/hello.html',{'data':name})
    else:
        form=NameForm()
        return render(request,'blog/hello.html',{'data':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/addpost/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def showstudent(request):

    data = Article.objects.all().order_by("-created_date")
    return render(request,'blog/post.html', {'data': data})


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

