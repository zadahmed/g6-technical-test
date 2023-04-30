from django.contrib import admin

from pulse_survey.survey.models import Result, Feedback


admin.site.register(Result)
admin.site.register(Feedback)
