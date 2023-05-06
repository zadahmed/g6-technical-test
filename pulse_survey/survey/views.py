import uuid

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from pulse_survey.survey.models import Result


def index(request):
    session_id = uuid.uuid4()
    start = request.GET.get("start")
    if start:
        return redirect(reverse("team", args=(session_id,)))
    return render(request=request, template_name="index.html", context={"session_id": session_id})


def team_view(request, session_id):
    errors = {}
    page_number = 1
    result, _ = Result.objects.get_or_create(session_id=session_id, page_number=page_number)
    teams = {"Team A", "Team B", "Team C"}
    chosen_team = None
    if result.data:
        chosen_team = result.data.get("team")
    if request.method == "POST":
        result.data = request.POST
        result.save()
        return redirect(reverse("location", args=(session_id,)))
    return render(request, "team_question.html", {"errors": errors, "teams": teams, "chosen_team": chosen_team})


def location_view(request, session_id):
    errors = {}
    page_number = 2
    result, _ = Result.objects.get_or_create(session_id=session_id, page_number=page_number)
    locations = {"London", "Manchester", "Glasgow", "York", "Bristol"}
    chosen_location = None
    if result.data:
        chosen_location = result.data.get("location")
    if request.method == "POST":
        result.data = request.POST
        result.save()
        # TODO - next page
        return render(request, "index.html", {"request": request, "errors": errors})
    return render(request, "location_question.html", {"errors": errors, "locations": locations, "chosen_location": chosen_location})

