from django.urls import path
from . import views


urlpatterns = [
    path('card/', views.card, name='card'),
    path('<int:kimchi_id>',views.detail, name="detail"),  #패스컨버터
    path('serch/', views.post_list, name="post_list"),
]
