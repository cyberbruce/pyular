from mimetypes import init
from django.shortcuts import render
from . import forms
from . import pyular
import time


def home(request):  
    
    context = {}
    form = forms.PyularForm(request.POST or None)
    context['form'] = form        
    if request.method == "POST":            
        if form.is_valid():
            try:
                result = pyular.PyularParse(
                    form.cleaned_data['expression'],
                    form.cleaned_data['sample']
                )            
                context['parse'] = result         
            except Exception as e:
                context['parse'] = None
                print(e)
                
        return render(request, "home/_index.html", context)
    else:
      return render(request, "home/index.html", context)
