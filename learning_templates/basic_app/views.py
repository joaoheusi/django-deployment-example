from django.shortcuts import render

# Create your views here.


def index(request):
    index_dict ={
        'text': 'lorem impsum dolor sinat',
        'number': '100'
    }
    return render(request, 'basic_app/index.html',context=index_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')