from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .models import *


class Login(view):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = Admin.get_admin_by_username(username)
        error_message = None

        if admin:
            flag = check_password(password, admin.password)
            if flag:
                request.session['admin'] = admin.inside

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')

            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Invalid'

        print(username, password)
        return render(request, 'login.html', {'error': error_message})

    def logout(request):
        request.session.clear()
        return redirect('login')


class AddEmployee(View):
    def get(self, request):
        return render(request, 'add.html')
