from django.urls import path, include
from .import views
app_name='movieapp'

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('add/',views.add_movie,name='add_movie'),
    path('', views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),

]
