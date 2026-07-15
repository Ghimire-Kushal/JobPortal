from django.shortcuts import render, redirect
from django.db import models

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from portal.models import Job
from .forms import ApplicantForm, UserRegisterForm, UserLoginForm

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def job_detail(request, pk):
    jobbbb = Job.objects.get(id=pk)
    return render(request, "job_detail.html", 
                  {"job": jobbbb, "form": ApplicantForm()})

@login_required # decorators
def handle_applicant(request, pk):
    print(request.user)
    form = ApplicantForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save()
        obj.user = request.user 
        obj.save()
    else:
        print(form.errors)
    return redirect("/")


@login_required
def get_applied_jobs(request):
    from portal.models import Applicant
    applicants = Applicant.objects.filter(
        user=request.user
    )
    return render(request, "application.html", {"applicants": applicants})



def root_redirect_view(request):
    return redirect("user-login")


@login_required
def dashboard_view(request):
    from portal.models import Company
    jobs = Job.objects.all().order_by("-created_at")

    query = request.GET.get("q", "").strip()
    if query:
        jobs = jobs.filter(
            models.Q(title__icontains=query) | models.Q(company__name__icontains=query)
        )

    selected_location = request.GET.get("location", "").strip()
    if selected_location:
        jobs = jobs.filter(company__location=selected_location)

    locations = (
        Company.objects.exclude(location="")
        .values_list("location", flat=True)
        .distinct()
        .order_by("location")
    )

    return render(request, "dashboard.html", {
        "jobs": jobs,
        "query": query,
        "selected_location": selected_location,
        "locations": locations,
    })


def user_register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data.get("username"),
                email = data.get("email")
            )
            user.set_password(data.get("password"))
            user.save()
            return redirect("/register")
    else:
        form = UserRegisterForm()
        print("form", form)
        return render(request, "register.html", {"form": form})

    
def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(
                    username=form.cleaned_data.get("username")
                )
            except User.DoesNotExist:
                #TODO: message invalid username
                return redirect("/login")
            if user.check_password(form.cleaned_data.get("password")):
                login(request, user)
                return redirect("/dashboard")
            else:
                # TODO: Message invalid password
                return redirect("/login")
    else:
        form = UserLoginForm()
        return render(request, "login.html", {"form": form})