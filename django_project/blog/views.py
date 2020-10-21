from django.shortcuts import render

posts = [
    {
        'author':'isaac',
        'title':'blog post 1',
        'content':'first blog content',
        'date_posted':'12/12/10'
    },
    {
        'author':'Judy',
        'title':'blog post 2',
        'content':'second blog content',
        'date_posted':'12/12/10'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})





