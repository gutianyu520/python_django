from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.conf import settings


def index(request):
    return render(request, 'booktest/indexes.html')


def myex(request):
    a = int('ab')
    return HttpResponse('hello')


def uplao(request):
    return render(request, 'booktest/upload.html')


def upload(request):
    pic1 = request.FILES['pic']
    fname = '%scars/%s' % (settings.MEDIA_ROOT, pic1.name)
    with open(fname, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse(fname)
    # with open(fname, 'w') as pic:


from .models import *
from django.core.paginator import *


def pageList(request, index=1):
    list = UserInfo.objects.all()
    pagena = Paginator(list, 1)
    page = pagena.page(int(index))
    context = {'page': page}
    return render(request, 'booktest/page.html', context)


def region(request):
    return render(request, 'booktest/region.html')


def region_select(request, pid):
    data = AreaInfo.objects.filter(parent_id=pid)
    list = []
    for i in data:
        list.append([i.pk, i.name, i.parent_id, i.level_id])
    print(list)
    return JsonResponse({'data': list})


def htmlEditor(request):
    return render(request, 'booktest/indexes.html')


from django.views.decorators.cache import cache_page
from django.core.cache import *


@cache_page(60)
def cache1(request):
    cache.set('key1', 'value1', 600)
    c1 = cache.get('key1')
    print(c1)
    cache.delete('key1')
    cache.clear()
    return HttpResponse('hello1')


def mysearch(request):
    return render(request, 'booktest/mysearch.html')


from task import *


def celery_common(request):
    show()
    return HttpResponse('ok')


def celery_delay(request):
    show.delay()
    return HttpResponse('ok')
