from django.urls import path
from . import views 
app_name="diagram"
urlpatterns = [
    path("",views.index,name="index")
]