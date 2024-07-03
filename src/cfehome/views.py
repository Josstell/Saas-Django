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
    my_context = {
        "page_title": "My old page",
        "total_visit_count": qs.count(),
        "page_visit_count": page_qs.count()
    }

    PageVisit.objects.create(path=request.path)

    return render(request, 'home.html', my_context)


def home_page_view_old(request, *qrgs, **kwargs):
    my_context = {
        "page_title": "My old page"
    }
    html_ = ""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text().format(**my_context)

    return HttpResponse(html_)
