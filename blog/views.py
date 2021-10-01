from django.shortcuts import render
from .models import  BlogDetail
# Create your views here.
def home(request):
    context={'blogs' : BlogDetail.objects.all(),'last' : BlogDetail.objects.last()}
    return render(request,"home.html",context)


def detail(request,slug):
        blog_obj = BlogDetail.objects.filter(slug=slug).first()
        context = {"blog":blog_obj}
        return render(request,"blog_detail.html",context)
