from django.urls import path
from .views import *

"""
URLs pattern for the SleepConditionAPI view, StepCondition1API view, and StepCondition2API view.
"""
urlpatterns = [
    path('sleep-condition/', SleepConditionAPI.as_view()),
    path('steps-condition-1/', StepCondition1API.as_view()),
    path('steps-condition-2/', StepCondition2API.as_view()),
]
