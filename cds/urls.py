from django.urls import path
from . import views

urlpatterns = [
    path('', views.CDView.as_view(), name='cds'),
    path('<int:pk>/rent/', views.CDRent.as_view(), name='cd_rent'),
    path('<int:pk>/unrent/', views.CDUnRent.as_view(), name='cd_unrent'),
    path('detail/<int:pk>/', views.CDDetail.as_view(), name='cd_detail'),
    path('new', views.CDNew.as_view(), name='cd_new'),
    path('<int:pk>/edit/', views.CDEdit.as_view(), name='cd_edit'),
    path('remove/<int:pk>', views.CDRemove.as_view(), name='cd_remove'),
    path('rentedcds/', views.RentedCDView.as_view(), name='rentedcds')
]
