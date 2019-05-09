from django.shortcuts import render
from .models import Results


def allresults(request):
    results = Results.objects
    mon = request.POST['mahina']
    yea = request.POST['saal']
    return render(request, 'results/allresults.html', {'results': results, 'month': mon, 'year': yea})
