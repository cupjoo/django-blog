
from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail'),

    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('today/', views.PostTAV.as_view(), name='post_today_archive'),
    path('search/', views.SearchFormView.as_view(), name='search'),

    path('add/', views.PostCreateView.as_view(), name='add'),
    path('change/', views.PostChangeLV.as_view(), name='change'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
