from django.http import HttpResponse
from kokowalk.models import User
import json

def user_list(request):
    print "request"
    print request
    print request.method
    req = request.META['QUERY_STRING']
    reqs = req.split('&')
    name = reqs[0].split('=')[1]
    adder = reqs[1].split('=')[1]
    
    obj, created = User.objects.get_or_create(name=name)
    if created:
        obj.counter = 0
        obj.save()

    count = 0;
    for object in User.objects.all():
        if object.name == name:
            object.counter = object.counter + int(adder)
            object.save()
        count = count + object.counter
        str_count = str(count)  # + 'haifuri wo mite'

    return HttpResponse(str_count, content_type='application/json')
