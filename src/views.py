from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Enquiry
from .forms import EnquiryForm
from django.http import JsonResponse
def home(request):
    form=EnquiryForm(request.POST or None)
    data={}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name']=form.cleaned_data.get('name')
            data['status']='ok'
            return JsonResponse(data)
        else:
            data['error']=form.errors
            return JsonResponse(data)



        


    return render(request, 'home.html' )
