from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import userRegistration
from .models import userLogin
from django.http import HttpResponse, HttpResponseRedirect
from .models import userSignUp
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'frontdesk/home.html')
def success_message(request):
    return HttpResponse("Registration has been done successfully")

def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userRegistration(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model = userSignUp()
            model.full_name = form.cleaned_data['full_name']
            model.business_type = form.cleaned_data['business_type']
            model.mobile_number = form.cleaned_data['mobile_number']
            model.email = form.cleaned_data['email']
            model.password = form.cleaned_data['password']
            model.save()
            # redirect to a new URL:
            messages.success(request, 'Form submitted successfully')
            #return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = userRegistration()
    return render(request, 'frontdesk/sign_up_form.html', {'form': form})

class userloginCreate(CreateView):
    model = userLogin
    fields = ['mobile_number', 'password']
