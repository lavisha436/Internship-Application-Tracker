from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import applications
from applications.forms import ApplicationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from applications.models import Application
from django.shortcuts import get_object_or_404

# Create your views here.
# Add-form
@login_required
def add_application(request):

    if request.method == "GET":

        form = ApplicationForm()

        return render(
            request,
            "add_applications.html",
            {"form": form}
        )

    else:

        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.user = request.user

            application.save()

            return redirect("home")


# home page
def home(request):

    if request.user.is_authenticated:

        applications = Application.objects.filter(user=request.user)

        total_applications = applications.count()
        interview_count = applications.filter(status="Interview").count()
        applied_count = applications.filter(status="Applied").count()
        offered_count = applications.filter(status="Offered").count()
        rejected_count = applications.filter(status="Rejected").count()
        recent_applications = applications.order_by("-id")[:5]

    else:

        total_applications = 0
        interview_count = 0
        applied_count = 0
        offered_count = 0
        rejected_count = 0
        recent_applications = []

    return render(
        request,
        "home.html",
        {
            "total_applications": total_applications,
            "interview_count": interview_count,
            "applied_count": applied_count,
            "offered_count": offered_count,
            "rejected_count": rejected_count,
            "recent_applications": recent_applications,
        },
    )


# register form
def register_user(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(request, "register_user.html", {"form": form})

# login form
def login_user(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("home")

    else:

        form = AuthenticationForm()

    return render(request, "login_user.html", {"form": form})

# logout user
def logout_user(request):

    logout(request)

    return redirect("login_user")


# application list
@login_required
def application_list(request):

    search = request.GET.get("search")

    applications = Application.objects.filter(user=request.user)

    if search:
        applications = applications.filter(company_name__icontains=search)

    return render(request, "applications_list.html", {"applications": applications})


# delete application
@login_required
def delete_application(request, id):

    application = get_object_or_404(Application, id=id, user=request.user)
    application.delete()

    return redirect("application_list")


@login_required
def edit_application(request, id):

    application = get_object_or_404(Application, id=id, user=request.user)

    if request.method == "GET":

        form = ApplicationForm(instance=application)

        return render(request, "edit_application.html", {"form": form})

    else:

        form = ApplicationForm(request.POST, instance=application)

        if form.is_valid():

            form.save()

            return redirect("application_list")
