from django.shortcuts import render
from .import forms


def index(request):
    return render(request,'basicapp/index.html/')

def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form =forms.FormName(request.POST)

        if form.is_valid():

            print("Sucesso")
            print("Nome :" + form.cleaned_data['nome'])
            print("Email :" + form.cleaned_data['email'])
            print("Texto:" + form.cleaned_data['text'])


    return render(request,'basicapp/form_page.html/',{'form':form})