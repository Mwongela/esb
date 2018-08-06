from django.urls import path
from api.views import *

urlpatterns = [
    path('pagestats', PageStatView.as_view(), name="pageStats"),
    path('group', GroupView.as_view(), name="group"),
    path('goal', GoalView.as_view(), name="goal")
]
