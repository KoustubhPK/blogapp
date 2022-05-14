from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_only


# Create your views here.

@unauthenticated_only
def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Wrong Username Or Password')
    return render(request, 'user/userlogin.html')

@unauthenticated_only
def UserRegister(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully, Please Login!')
            return redirect('userlogin')
    else:
        user_form = UserRegisterForm()
    return render(request, 'user/userregister.html', {'user_form':user_form})

def UserLogout(request):
    logout(request)
    #return redirect('userlogin')
    return render(request, 'user/userlogout.html')

@login_required(login_url='userlogin')
def UserProfile(request):
    return render(request, 'user/userprofile.html')

@login_required(login_url='userlogin')
def EditProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile Updated Successfully!')
            return redirect('userprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
             
    context = {
        'u_form': u_form,
        'p_form': p_form
        }
    return render(request, 'user/editprofile.html', context)


def Userdetail(request):
    return render(request, 'user/userdetail.html')

def UserTerms(request):
    return render(request, 'user/terms_and_conditions.html')