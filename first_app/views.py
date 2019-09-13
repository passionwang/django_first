# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# welcome
def index(request):

    #return HttpResponse(u"欢迎光临！ ---彪彪！")
    return render(request, 'first_app/home_extends.html')


# add
def add(request):

    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)

    return HttpResponse(str(c))


# add2
def add2(request, a, b):

    c = int(a) + int(b)
    return HttpResponse(str(c))


# variable 使用
def variable(request):

    string = u"好好学习，天天向上！"
    return render(request, 'first_app/variable.html', {'string': string})


# for_user 使用
def for_use(request):

    tmp = ['one', 'two', 'three', 'four']
    return render(request, 'first_app/for.html', {'tmp': tmp})


