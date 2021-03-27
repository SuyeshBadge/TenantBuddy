from django.shortcuts import redirect, render
from main.models import *
import base64

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def rooms(request):
    return render(request, 'rooms.html')


def owner(request, Oid):
    print(Oid)
    s2byt = Oid.encode("ascii")
    s2b64byt = base64.b64decode(s2byt)
    key1 = s2b64byt.decode("ascii")
    print(key1)
    uid, fname, lname, login = key1.split('_')
    user = Owner.objects.get(oId=uid)
    return render(request, 'owner.html', {'user': user, 'login': login})


def register(request):
    if request.method == "POST":
        user = Owner()
        user.oFname = request.POST.get("fname")
        user.oLname = request.POST.get("lname")
        user.oEmail = request.POST.get("email")
        user.oMobile = request.POST.get("mobile")
        user.oDOB = request.POST.get("dob")
        user.oGender = request.POST.get("Gender")
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if Owner.objects.filter(oEmail=user.oEmail).exists():
            return render(request, 'register.html', {'error': "Email Already Exist "})
        else:
            if pass1 == pass2:
                user.oPassword = pass1
                user.save()
                print('done')
                print(
                    user.oFname,
                    user.oLname,
                    user.oDOB,
                    user.oEmail
                )
                s1 = f'{user.oId}_{user.oFname}_{user.oLname}_True'
                s1byt = s1.encode("ascii")
                s1b64byt = base64.b64encode(s1byt)
                key = s1b64byt.decode("ascii")
                return redirect('owner', key)
            else:
                return render(request, 'register.html', {'error': "Password Mismatched"})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        if Owner.objects.filter(oEmail=request.POST.get("email")).exists():
            user = Owner.objects.get(oEmail=request.POST.get("email"))
            if user.oPassword == request.POST.get("pass"):
                print("Login Success")
                s1 = f'{user.oId}_{user.oFname}_{user.oLname}_True'
                s1byt = s1.encode("ascii")
                s1b64byt = base64.b64encode(s1byt)
                key = s1b64byt.decode("ascii")
                return redirect('owner', key)
            else:
                return render(request, 'login.html', {'error': "Invalid Pass"})
        else:
            return render(request, 'login.html', {'error': "Email Doesn't Exist"})
    else:
        return render(request, 'login.html')
