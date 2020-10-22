from django.shortcuts import render
from .models import squirrel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Min, Max

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
        form=squirrel(request.GET)
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
    total = len(squirrel.objects.all())
    la_sum = squirrel.objects.all().aggregate(minimum=Min('latitude'),maximum=Max('latitude'))
    lo_sum = squirrel.objects.all().aggregate(minimum=Min('longitude'),maximum=Max('longitude'))
    age_juvenile = squirrel.objects.filter(age='juvenile').count()
    age_adult = squirrel.objects.filter(age='adult').count()
    context ={'total':total,'la_sum':la_sum,'lo_sum':lo_sum,'age_juvenile':age_juvenile,'age_adult':age_adult}
    return render(request, 'app/stats.html', context)


