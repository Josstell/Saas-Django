from visits.models import PageVisit
import pathlib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.conf import settings

LOGIN_URL = settings.LOGIN_URL


this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *qrgs, **kwargs):
    print(request.user.is_authenticated, request.user)
    return about_page(request, *qrgs, **kwargs)


def about_page(request, *qrgs, **kwargs):

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


@login_required
def user_only_view(request, *args, **kwargs):
    return render(request, "protected/user-only.html")


@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "protected/staff-only.html")
