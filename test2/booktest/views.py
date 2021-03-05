from django.http import HttpResponse
from django.shortcuts import render,redirect
from PIL import Image,ImageDraw,ImageFont
import random

# Create your views here.
from .models import BookInfo


def index(request):
    book = BookInfo.objects.get(pk=1)
    book2 = BookInfo.objects.all()
    context = {'book': book, 'list': book2}
    return render(request,'booktest/indexes.html', context)


def base(request):
    context = {'t1': '<h1>asjdad<h1>'}
    return render(request,'booktest/base.html', context)

def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return render(request, 'booktest/csrf2.html',{'uname': uname})


import io
# verify code
def verifyCode(request):
    # create RGB color
    backgroundColor = (random.randrange(50, 100),random.randrange(50, 100),0,)
    width = 100
    height = 25
    # create image
    image = Image.new('RGB', (width, height), backgroundColor)
    # create pen
    font = ImageFont.truetype('FreeMono.ttf',24)
    draw = ImageDraw.Draw(image)
    text = 'ABCD'
    # for t in text:
    draw.text((0, 0), text,(255,255,255),font)
    buf = io.BytesIO()
    image.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')

