from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),             
    path("category/<category>/", views.blog_category, name="category"),
    path("<int:pk>/", views.blog_detail, name="detail"),    
]
