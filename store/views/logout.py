from django.shortcuts import render,redirect

def Logout(request):
    request.session.clear()
    return redirect("login")
