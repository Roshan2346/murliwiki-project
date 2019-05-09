from django.shortcuts import render
from .models import Results


def allresults(request):
    results = Results.objects.all()
    mon = request.POST['mahina']
    yea = int(request.POST['saal'])
    pdf_url = {}
    ti = []
    da = []

    for i in results:
        m = i.month
        y = i.year
        f = i.file
        u = f.url
        t = i.title
        d = i.date
        dt = d + " \u2192 " + t

        if (mon == 'all' and yea == y):
            pdf_url[dt] = u

        elif (mon == m and yea == y):
            pdf_url[dt] = u

    if (len(pdf_url) == 0):
        return render(request, 'results/allresults.html', {'y': yea, 'error': 'No Murlis found for this period of time. Try changing the month...'})
    else:
        pl = pdf_url.items()
        return render(request, 'results/allresults.html', {'y': yea, 'pl': pl})
