from django.shortcuts import render

# Create your views here.
def homepagecall(request):
    return render(request,'adminapp/projecthomepage.html')



def loginpagecall(request):
    return render(request,'adminapp/LoginPage.html')

def registerpagecall(request):
    return render(request, 'adminapp/Register.html')


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user:  # Only log in if the user is successfully authenticated
            auth.login(request, user)  # Log in the user
            if len(username) == 4:
                messages.success(request, 'Login successful as Trainer!')
                return redirect('trainerapp:trainerhomepage')
            elif len(username) == 10:
                messages.success(request, 'Login successful as Employee!')
                return redirect('employeeapp:employeehomepage')
            else:
                messages.error(request, 'Username length does not match trainer or employee criteria.')
                return render(request, 'adminapp/LoginPage.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/LoginPage.html')
    else:
        return render(request, 'adminapp/LoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')
