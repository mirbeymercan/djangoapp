from email import message
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
# Cross Site Request Forgery : 3. Kişiler) Formlarımızı post yardımıyla kaydediyoruz arada 3. kişiler (man in the middle) bu oturum bilgilerini çalabilir. Bu yüzden CSRF kullanıyoruz
# csrf token register.html dosyasına dahil edildi.

# Kullanıcı Kayıt

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():                         # clean fonksiyonun kullanımı
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()

            login(request, newUser)             # Kayıt olduktan sonra giriş yapıldı
            messages.success(request, 'You have successfully registered. Welcome!')

            return redirect('index')                   # anasayfaya yönlendirildi

        context = {
            'form': form
        }
        return render(request, 'register.html', context)

    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)

    """
    form = RegisterForm(request.POST or None)           # POST olursa POST, GET olursa None kısmı çalışacak

    if form.is_valid():
        username = form.changed_data.get('username')
        password = form.changed_data.get('password')

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()

        login(request, newUser)

        return redirect('index')
    
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
    """


# Kullanıcı Giriş

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username = username, password = password)      # authenticate : kullanıcının olup olmadığını sorgular

        if user is None:        # kullanıcı yoksa
            messages.info(request, 'Username or Password is Incorrect!')
            return render(request, 'login.html', context)
        
        else:
            messages.success(request, 'Log in was successfully. Welcome.')
            login(request, user)
            return redirect('index')
    

    return render(request, 'login.html', context)


# Kullanıcı Çıkış

def logoutUser(request):
    logout(request)
    messages.success(request, 'Sign out was successfully. Goodbye!')
    return redirect('index')