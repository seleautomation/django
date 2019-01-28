from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import userRegistration
from .models import userLogin
from django.http import HttpResponse, HttpResponseRedirect
from .models import userSignUp
from django.contrib import messages
from .forms import userFormLogin

# Create your views here.
def home(request):
    return render(request, 'frontdesk/home.html', {"form": userFormLogin()})
def success_message(request):
    return HttpResponse("Registration has been done successfully")




def login(request):
    if request.method == 'POST':
        form = userFormLogin(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']
            if userLogin.objects.filter(mobile_number=mobile).exists():
                userCredentials = userLogin.objects.get(mobile_number=mobile)
                if userCredentials.password == password:
                    return HttpResponse("<h1>User has been logged-in successfully</h1>")
                else:
                    password_error_message = "Wrong password"
                    pass_error = True
                    return render(request, 'frontdesk/home.html', {'form': userFormLogin(), 'password_error_message':password_error_message, 'pass_error':pass_error})
            else:
                mobile_error_message = "Oops, we don’t recognize this mobile number"
                mobile_error = True
                return render(request, 'frontdesk/home.html', {'form': userFormLogin(), 'mobile_error_message':mobile_error_message, 'mobile_error':mobile_error})
        else:
            return HttpResponse("form not validated")
    else:
        return render(request, 'frontdesk/home.html', {'form': userFormLogin()})



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

            login_model = userLogin()
            login_model.mobile_number = form.cleaned_data['mobile_number']
            login_model.password = form.cleaned_data['password']
            login_model.save()
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
