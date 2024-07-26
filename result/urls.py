# This file is relevant to result\views.py
# This file maps user request to the appropriate view.

from django.urls import path        # so we have urlpatterns
from . import views                 # so we have views functions associated with urlpatterns

# We define urlpatterns to link them to specific view functions.
urlpatterns = [
    path('', views.predictor, name='predictor'),
    # user visits website.com/result url, views.result executed, the url pattern name is 'result'
    path('result/', views.result, name='result'),
]