from django.shortcuts import redirect, render
from main.models import Room, Owner
import base64
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def rooms(request):
    if request.method == 'POST':
        print("nice")
        rooms = rooms = Room.objects.all().filter(
            rCity=str(request.POST.get('city')).lower()).order_by('-rPrice')
        print(request.POST.get('city').lower())
        return render(request, 'rooms.html', {'list': rooms})

    else:
        rooms = Room.objects.all().order_by('-rPrice')
        return render(request, 'rooms.html', {'list': rooms})


def addroom(request, Oid):
    print(Oid)
    s2byt = Oid.encode("ascii")
    s2b64byt = base64.b64decode(s2byt)
    key1 = s2b64byt.decode("ascii")
    print(key1)
    uid, fname, lname, login = key1.split('_')
    user = Owner.objects.get(oId=uid)
    if request.method == 'POST':
        room = Room()
        room.rOid = user
        room.rAddress = request.POST.get("area")
        room.rCity = request.POST.get("city").lower()
        room.rState = request.POST.get("state")
        room.rShare = request.POST.get("share")
        room.rBathroom = request.POST.get("bathroom")
        room.rType = request.POST.get("rtype")
        room.rPrice = request.POST.get("price")
        room.rGirlsOnly = request.POST.get("girls")
        room.rPic = request.FILES['pic']
        user.oRooms += 1
        room.save()
        user.save()

        return render(request, 'addroom.html', {'user': user, 'login': login, 'key': Oid, 'error': 'Room Added SuccessFully'})

    else:
        return render(request, 'addroom.html', {'user': user, 'login': login, 'key': Oid})


def owner(request, Oid):
    print(Oid)
    s2byt = Oid.encode("ascii")
    s2b64byt = base64.b64decode(s2byt)
    key1 = s2b64byt.decode("ascii")
    print(key1)
    uid, fname, lname, login = key1.split('_')
    user = Owner.objects.get(oId=uid)
    rooms = Room.objects.all().filter(rOid=user)
    print(rooms)
    return render(request, 'owner.html', {'user': user, 'login': login, 'key': Oid, 'error': 'Login Success', 'list': rooms})


def profile(request, Oid):
    print(Oid)
    s2byt = Oid.encode("ascii")
    s2b64byt = base64.b64decode(s2byt)
    key1 = s2b64byt.decode("ascii")
    print(key1)
    uid, fname, lname, login = key1.split('_')
    user = Owner.objects.get(oId=uid)
    if request.method == "POST":
        user.oFname = request.POST.get("fname")
        user.oLname = request.POST.get("lname")
        user.oMobile = request.POST.get("mobile")
        user.oGender = request.POST.get("Gender")
        user.oProfile = request.FILES['pic']
        user.save()
        return render(request, 'profile.html', {'user': user, 'login': login, 'key': Oid, 'error': "Profile Updated Successfully"})

    else:
        return render(request, 'profile.html', {'user': user, 'login': login, 'key': Oid})


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
                return render(request, 'login.html', {'error': "Invalid Password"})
        else:
            return render(request, 'login.html', {'error': "Email Doesn't Exist"})
    else:
        return render(request, 'login.html')


def delroom(request, Oid):
    s2byt = Oid.encode("ascii")
    s2b64byt = base64.b64decode(s2byt)
    key1 = s2b64byt.decode("ascii")
    print(key1)
    uid, fname, lname, login = key1.split('_')
    user = Owner.objects.get(oId=uid)
    if request.method == 'POST':
        roomid = request.POST.get('roomid')
        room1 = Room.objects.get(rId=roomid)
        user.oRooms -= 1
        user.save()
        room1.delete()
        return redirect('owner', Oid)
    else:
        return redirect('owner', Oid)
