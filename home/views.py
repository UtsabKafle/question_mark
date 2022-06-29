import re
from django.shortcuts import redirect, render
from .models import data
# Create your views here.
def home(request):
    if request.method == "POST":
        date = request.POST['date']
        title = request.POST['title']
        content = request.POST['content']
        if title != '' and content != '':
            ob = data.objects.create(date=date,title=title,content=content)
    return render(request,'temp.html',{})

def page_view(request,id):
    data_ = data.objects.get(id=id)
    context = {
        'date':str(data_.date),
        'title':str(data_.title),
        'content':data_.content
    }
    if request.method == "POST":
        date = request.POST['date']
        title = request.POST['title']
        content = request.POST['content']
        data_.date = date
        data_.title = title
        data_.content = content
        data_.save()
        return redirect(archive)
    
    return render(request,'pages.html',context)

def archive(request):
    archives = data.objects.all()
    context = {
        'archives':reversed(archives)
    }
    return render(request,'archives.html',context)