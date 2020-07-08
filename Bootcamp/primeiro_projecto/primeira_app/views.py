from django.shortcuts import render
from django.http import HttpResponse
from primeira_app.models import Topic , Paginaweb , AccessRecord

def index(request):
    paginaweb_list = AccessRecord.objects.order_by('data')
    my_dic= {'access_records':paginaweb_list}
    return render(request,'primeira_app/index.html',context=my_dic)

# Create your views here.
