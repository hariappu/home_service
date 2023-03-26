from django.shortcuts import render,redirect
from home_web.forms import Userprofileform
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from home_web.models import Userprofile



# Create your views here.
class UserProfileCreateView(CreateView):
    form_class=Userprofileform
    model=Userprofile
    template_name="profile-add.html"
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"


class ProfileUpdateView(UpdateView):
    form_class=Userprofileform
    model=Userprofile
    template_name="profile-edit.html"
    success_url=reverse_lazy("home")

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")