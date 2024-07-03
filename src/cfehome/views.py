import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *qrgs, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(
        path=request.path
    )

    try:
        percent = (page_qs.count() / qs.count())*100
    except:
        percent = 0

    my_context = {
        "page_title": "My old page",
        "total_visit_count": qs.count(),
        "percent": percent,
        "page_visit_count": page_qs.count()
    }

    PageVisit.objects.create(path=request.path)

    return render(request, 'home.html', my_context)


def about_page(request, *qrgs, **kwargs):

    return home_page_view(request, *qrgs, **kwargs)
