from django.shortcuts import render
from django.http import HttpResponse

from pulse_survey.survey.models import Result


def index(request):
    return render(request=request, template_name="index.html")


def team_view(request):
    errors = {}
    if request.method == "POST":
        # add session)id
        Result(data=request.data).save()
        return render(request, template_name="team_question.html", context={"request": request, "errors": errors})

    #"session_id": session_id, 
    return render(request, template_name="team_question.html", context={"request": request, "errors": errors})
