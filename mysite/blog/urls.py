
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('today/', views.PostTAV.as_view(), name='post_today_archive'),
]
