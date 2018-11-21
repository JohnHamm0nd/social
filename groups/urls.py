from django.urls import path
from . import views
app_name = 'groups'

urlpatterns = [
    path('',views.GroupList.as_view(),name='list'),
    path('create/',views.GroupCreate.as_view(),name="create"),
    path('posts/in/<slug>',views.GroupDetail.as_view(),name="detail"),
    path('join/<slug>', views.GroupJoin.as_view(), name='join'),
    path('leave/<slug>', views.GroupLeave.as_view(), name='leave'),
]