from django.urls import path
from college import  views

from college.views import SignUpView

from college.views  import homepage,studentcell,addstd,stdreport

urlpatterns = [

path('studentcell/',studentcell),
path('addstd/',addstd),
path('stdreport/',stdreport),
path('signup/',SignUpView.as_view(), name="signup"),

]
