from django.shortcuts import render
from .models import squirrel
from .forms import apprequestform
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum

def get_post_request(request):
    if request.method=='POST':
        form=squirrel(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'error':form.error},status=400)
    else:
        form=squirrel(request.GET)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'error':form.error},status=400)
def get_request(request):
    if request.method=='GET':
        form=apprequestform(request.GET)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'error':form.error},status=400)
    return JsonResponse({},status=405)


def map(request):
    sightings=squirrel.objects.all()[:100]
    context={'sightings':sightings}
    get_request(request)
    return render(request, 'app/map.html',context)
def sightings(request):
    sightings = squirrel.objects.all()
    context = {'sightings': sightings}
    return render(request, 'app/sightings.html', context)
def unique_squirrel_id(request,squiid):
    sightings = squirrel.objects.get(squirrel_id=squiid)
    context = {'sightings': sightings}
    if request.method=='POST':
        form = squirrel(request.POST)
    elif request.method=='GET':
        form = squirrel(request.GET)
    else:
        return JsonResponse({},status=405)
    sightings.latitude=form.latitude
    sightings.longitude=form.longitude
    sightings.squirrel_id=form.squirrel_id
    sightings.shift=form.shift
    sightings.date=form.date
    sightings.age=form.age
    return render(request, 'app/id.html', context)
def add(request):
    get_post_request(request)
    sightings = squirrel()
    context = {'sightings': sightings}
    return render(request, 'app/add.html', context)
def stats(request):
    la_sum = squirrel.aggregate(minimum=Min('latitude'),maximum=Max('latitude'))
    lo_sum = squirrel.aggregate(minimum=Min('longitude'),maximum=Max('longitutde'))
    id_sum=0
    for i in squirrel.objects.filter('squirrel_id'):
        id_sum+=1
    shift_am=0
    shift_pm=0
    for i in squirrel.objects.filter('shift'):
        if i =='PM':
            shift_pm+=1
        else:
            shift_am+=1
    age_juvenile=0
    age_adult=0
    age_unknown=0
    for i in squirrel.objects.filter('age'):
        if i=="Juvenile":
            age_juvenile+=1
        elif i=="Adult":
            age_adult+=1
        else:
            age_unknown+=1
    context = {'la_sum':la_sum,'lo_sum':lo_sum,'id_sum':id_sum,'shift_am':shift_am,'shift_pm':shift_pm,'age_juvenile':age_juvenile,'age_adult':age_adult,'age_unknown':age_unknown}
    return render(request, 'app/stats.html', context)


