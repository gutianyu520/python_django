# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect


# Create your views here.


def index(request):
    # return HttpResponse("hello world "+request.path)
    # return HttpResponse("hello world "+request.method)
    # return HttpResponse("hello world "+request.is_ajax())
    return render(request, "booktest/indexes.html")


def test1(request):
    # a1 = request.GET['a']
    # a1 = request.GET.get('a')
    # a1 = request.GET.getlist('a')
    a1 = request.POST.get('a')
    print(a1)
    context = {'a': a1}
    return render(request, 'booktest/test1.html', context)


def detail(request, p1, p2, p3):
    return HttpResponse(p1 + p2 + p3)


def test2(request):
    a1 = request.POST.get('a')
    print(a1)
    context = {'a': a1}
    return render(request, 'booktest/test1.html', context)


# cookie test
def cookie_set(request):
    resp = HttpResponse()
    # set cookie
    # resp.set_cookie('h1','abc')
    # get cookie
    cookies = request.COOKIES
    # python2 find key in cookies --> cookie.has_key('keyName')
    # python3 find key in cookies --> 'keyName' in cookie
    if 'h1' in cookies:
        resp.write(cookies['h1'])
    return resp


# redirect test
def redTest(request):
    # return HttpResponseRedirect('cookie_set/')
    return redirect('cookie_set/')


# session practice
def session1(request):
    uname = request.session.get('session_name', 'no login')
    context = {'uname': uname}
    return render(request, 'booktest/session1.html', context)


def session2(request):
    uname = None
    context = {'uname': uname}
    return render(request, 'booktest/session2.html', context)


def session3(request):
    del request.session['session_name']
    return redirect('/booktest/session1/')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['session_name'] = uname
    request.session.set_expiry(0)
    return redirect('/booktest/session1/')

# session default save in db
# so before use session, you should migrate project
# commandline: (python manage.py migrations)(python manage.py migrate)
# or use other db setting
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# SESSION_ENGINE = 'redis_session.session'
# SESSION_REDIS_HOST = 'localhost'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 0
# SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'session'



