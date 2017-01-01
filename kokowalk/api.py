from django.http import HttpResponse
from kokowalk.models import User
import json

def user_list(request):
    print "request"
    print request
    req = request.META['QUERY_STRING']
    reqs = req.split('&')
    name = reqs[0].split('=')[1]
    adder = reqs[1].split('=')[1]
    print name
    print adder

    
    m = User.objects.select_related().get(name=name)
    print m.name
    print m.counter
    m.counter = m.counter + int(adder)
    m.save()

    return HttpResponse(m.counter, content_type='application/json')
        
    
    #return HttpResponse(_json, content_type='application/json')
