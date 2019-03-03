from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader, RequestContext
from django.urls import reverse

from .models import Profile, UserConcert, UserConcertMedia

# Create your views here.
def index(request):
    return render(request, 'index.html')