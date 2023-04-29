from django.shortcuts import render
from django.views.generic import TemplateView,CreateView

def indexfunc(request):
    return render(request,'index.html',{'a':100})

class News(TemplateView):
    template_name = 'news.html'
class Store(TemplateView):
    template_name = 'store.html'
class Look(TemplateView):
    template_name = 'look.html'
class Video(TemplateView):
    template_name = 'video.html'
class About(TemplateView):
    template_name = 'about.html'
class Stockist(TemplateView):
    template_name = 'stockist.html'