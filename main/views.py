from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def createProfile(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        age = request.POST['age']
        profession = request.POST['profession']

        newUserProfile = Profile(
            firstName = firstName,
            lastName = lastName,
            email = email,
            age = age,
            profession = profession,
        )

        newUserProfile.save()

        success = "Profile Created Successfully for " + firstName
        return HttpResponse(success)