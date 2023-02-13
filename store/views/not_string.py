
from django.shortcuts import HttpResponseRedirect
def not_String(str):
    str="not"

    return HttpResponseRedirect("hello")
