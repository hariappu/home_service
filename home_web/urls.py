from django.urls import path
from home_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("profiles/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profiles/detail",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profiles/<int:pk>/edit",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("signout",views.SignoutView.as_view(),name="logout"),
]