import datetime
import urllib
import urllib2
import json
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def today(request):
    today =datetime.date.today()
    tomorrow=today+datetime.timedelta(days=1)
    DATEFORMAT='%Y%m%d'
    Today=today.strftime(DATEFORMAT)
    Tomorrow=tomorrow.strftime(DATEFORMAT)
    url='http://news.at.zhihu.com/api/1.2/news/before/'+Tomorrow
    result=json.load(urllib.urlopen(url))
    stories=result['news']
    t = get_template('hah.html')
    html = t.render(Context({'Today': Today,'stories':stories}))
    return HttpResponse(html)

def someday(request,date):
    theday=datetime.date(int(date[0:4]),int(date[4:6]),int(date[6:8]))
    thedaytomorrow=theday+datetime.timedelta(days=1)
    DATEFORMAT='%Y%m%d'
    Theday=theday.strftime(DATEFORMAT)
    Thedaytomorrow=thedaytomorrow.strftime(DATEFORMAT)
    url='http://news.at.zhihu.com/api/1.2/news/before/'+Thedaytomorrow
    result=json.load(urllib.urlopen(url))
    stories=result['news']
    t = get_template('hah.html')
    html = t.render(Context({'Today': Theday,'stories':stories}))
    return HttpResponse(html)
