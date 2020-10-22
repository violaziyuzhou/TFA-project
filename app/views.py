from django.shortcuts import render
from .models import squirrel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Min, Max
from .forms import Form





def map(request):
    sightings=squirrel.objects.all()[:100]
    context={'sightings':sightings}

    return render(request, 'app/map.html',context)
def sightings(request):
    sightings = squirrel.objects.all()
    context = {'sightings': sightings}
    return render(request, 'app/sightings.html', context)
def unique_squirrel_id(request,squiid):
    sightings = squirrel.objects.get(squirrel_id=squiid)
    form = Form(request.POST,instance=sightings)
    context = {'form': form}
    if form.is_valid():
        sightings=form.save()
        sightings.save()
    else:   
        return render(request, 'app/id.html', context)
def add(request):
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Form()
        context = {'form':form}
    return render(request, 'app/add.html', context)
def stats(request):
    total = len(squirrel.objects.all())
    la_sum = squirrel.objects.all().aggregate(minimum=Min('latitude'),maximum=Max('latitude'))
    lo_sum = squirrel.objects.all().aggregate(minimum=Min('longitude'),maximum=Max('longitude'))
    age_juvenile = squirrel.objects.filter(age='juvenile').count()
    age_adult = squirrel.objects.filter(age='adult').count()
    context ={'total':total,'la_sum':la_sum,'lo_sum':lo_sum,'age_juvenile':age_juvenile,'age_adult':age_adult}
    return render(request, 'app/stats.html', context)


