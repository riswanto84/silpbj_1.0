from django.urls import path
from . import views

app_name = 'knowledge_base'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tambah_pengetahuan/', views.tambah_pengetahuan, name='tambah_pengetahuan'),
    ]