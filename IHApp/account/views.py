from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm
# Create your views here.

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", messages.add_message(request, messages.ERROR, "Yetkiniz YOK!"))

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #user ile eşleştirme
            user = authenticate(request, username = username, password = password)
            
            #user bilgisi varsa
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı.")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, "account/login.html", {"form":form})
        else:
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render (request, "account/login.html",{"form":form})

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username = username, password = password)
            login(request, user)
            messages.info(request,"Hesap başarıyla oluşturuldu.")
            return redirect("index")
        else:
            return render(request,"account/register.html", {"form":form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form": form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"parola güncellendi!")
            logout(request)
            messages.info(request,"Yeni şifre ile giriş yapınız.")
            return redirect("user_login")
        else:
            return render(request,"account/change-password.html", {"form":form})
    form = UserPasswordChangeForm(request.user)
    return render(request, "account/change-password.html", {"form":form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Çıkış Başarılı.")
    return redirect ("index")
