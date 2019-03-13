from django.shortcuts import render, render_to_response
from web.redisFunc import redisConn
# Create your views here.


def index(request):

    tmpdata = redisConn().getBlogInfo('9_1552461322')
    datalist = [tmpdata]
    return render(request, 'index.html', {'data': datalist})
