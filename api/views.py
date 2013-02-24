from django.views.decorators.csrf import csrf_exempt
from vReport.models import *
from django.http import *
from django.shortcuts import render_to_response, get_object_or_404
from aggregators import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
def report(request):
    if request.method == 'POST':
        print "Received a text message with content ", request.POST[u'Body'], " from ", request.POST[u'From']
        phone_from = request.POST[u'From'].replace("+","")
        message = request.POST[u'Body']
        
        values = message.split(".")
        values = [int(x) for x in values]
        
        r = Report()
        owner = IndividualUser.objects.get(phone=phone_from)
        print "Owner ", owner

        r.owner = owner
        
        r.supplemented_small = values[0]
        r.supplemented_big = values[1]
        r.dewormed = values[2]
        
        r.save()
        return HttpResponse(status=200)
    raise Http404

@login_required()
def getAggregateData(request):
    up = UserProfile.objects.get(user = request.user)

    if (DistrictUser.objects.filter(user = up)):
        level = DistrictUser.objects.get(user = up)
    elif (RegionalUser.objects.filter(user = up)):
        level = RegionalUser.objects.get(user = up)
    elif (NationalUser.objects.filter(user = up)):
        level = NationalUser.objects.get(user = up)

    result = aggregateDistrict(up)
    data = {
        'small': result[0],
        'large': result[1],
        'worms': result[2],
        'target_small': level.target_small,
        'target_big': level.target_big,
        'target_dewormed': level.target_dewormed,
        'small_portion' : float(100.0*result[0]/level.target_small),
        'big_portion' : float(100.0*result[1]/level.target_big),
        'worm_portion' : float(100.0*result[2]/level.target_dewormed),
    }

    print request.user.is_authenticated()
    return render_to_response('api/smallNums.html', data, context_instance=RequestContext(request))
