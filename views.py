from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


def index(request, tags):
    return render(request, 'article/index.html')

def article(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'article.html',
        context={'tags': tags},
    )
