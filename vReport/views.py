from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from vReport.models import *
from vReport.forms import *
from django.shortcuts import render_to_response, get_object_or_404
from api.aggregators import *

# Create your views here.

def welcome(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return render_to_response('vReport/welcome.html', {}, context_instance=RequestContext(request))

@login_required()
def index(request):
    #print "printing "
    #print DistrictUser.objects.all()[0].name
    reports = []
    distAndres = []
    regioAndres = []

    up = UserProfile.objects.get(user = request.user)


    if (DistrictUser.objects.filter(user = up)):
        du = DistrictUser.objects.get(user = up)
        for individual in du.individuals.all():
            reports.extend(individual.reports.all())
    elif (RegionalUser.objects.filter(user = up)):
        ru = RegionalUser.objects.get(user = up)
        dists = ru.districts.all()
        for dist in dists:
            distAndres.append((dist, aggregateDistrict(dist.user)))
    elif (NationalUser.objects.filter(user = up)):
        nu = NationalUser.objects.get(user = up)
        regis = nu.regions.all()
        for regi in regis:
            regioAndres.append((regi, aggregateDistrict(regi.user)))


    return render_to_response('vReport/index.html', {'userprofile':up, 'reports':reports, 'districts':distAndres, 'regions': regioAndres}, context_instance=RequestContext(request))

@login_required
def pw_success(request):
    return render_to_response('vReport/pw_success.html', {}, context_instance=RequestContext(request))

@login_required
def about(request):
    return render_to_response('vReport/about.html', {}, context_instance=RequestContext(request))

@login_required
def addReporter(request):

    up = UserProfile.objects.get(user = request.user)

    if request.method == 'POST':

        if (DistrictUser.objects.filter(user = up)):
            du = DistrictUser.objects.get(user = up)
            form = IndividualReporterForm(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                name = form.cleaned_data['name']
                iu = IndividualUser(
                    name=name,
                    phone=phone,
                    district=du
                    )
                iu.save()
                return HttpResponseRedirect('/')
        elif (RegionalUser.objects.filter(user = up)):
            ru = RegionalUser.objects.get(user = up)
            form = UserProfileReporterForm(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                name = form.cleaned_data['name']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                target_small = form.cleaned_data['target_small']
                target_big = form.cleaned_data['target_big']
                target_dewormed = form.cleaned_data['target_dewormed']

                user=User.objects.create_user(username, '', password)
                user.save()

                up = UserProfile(
                    user=user,
                    name=name,
                    phone=phone
                    )
                up.save()

                du = DistrictUser(
                    user=up,
                    regional=ru,
                    target_small=target_small,
                    target_big=target_big,
                    target_dewormed=target_dewormed
                    )
                du.save()
                return HttpResponseRedirect('/')
        elif (NationalUser.objects.filter(user = up)):
            nu = NationalUser.objects.get(user = up)
            form = UserProfileReporterForm(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                name = form.cleaned_data['name']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                target_small = form.cleaned_data['target_small']
                target_big = form.cleaned_data['target_big']
                target_dewormed = form.cleaned_data['target_dewormed']

                user=User.objects.create_user(username, '', password)
                user.save()

                up = UserProfile(
                    user=user,
                    name=name,
                    phone=phone
                    )
                up.save()

                ru = RegionalUser(
                    user=up,
                    national=nu,
                    target_small=target_small,
                    target_big=target_big,
                    target_dewormed=target_dewormed
                    )
                ru.save()
                return HttpResponseRedirect('/')

    else:
        if (DistrictUser.objects.filter(user = up)):
            form = IndividualReporterForm()
            du = DistrictUser.objects.get(user = up)
            reporters = du.individuals.all()

        elif (RegionalUser.objects.filter(user = up)):
            form = UserProfileReporterForm()
            ru = RegionalUser.objects.get(user = up)
            reporters = ru.districts.all()
        else:
            form = UserProfileReporterForm()
            nu = NationalUser.objects.get(user = up)
            reporters = nu.regions.all()

    templateInfo = {
        'form': form,
        'reporters': reporters
    }

    return render_to_response('vReport/add.html', templateInfo, context_instance=RequestContext(request))

# handle accept/deny reports

@login_required
def approveReport(request):
    report = get_object_or_404(Report,pk=request.GET['report_id'])
    print report
    report.approved = True
    report.save()
    return index(request)

@login_required
def denyReport(request):
    report = get_object_or_404(Report,pk=request.GET['report_id'])
    report.delete()
    return index(request)
    


