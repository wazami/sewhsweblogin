#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log.models import Club

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

def club_specific_view(request):
    #I should have a club id associated
    club = Club.name
    if club.owner is not request.user:
        print('NOPE!')
        #redirect this dude to an HTML page saying error?
        return render(request, "error_page.html")
	else:
		return render(request, #html file with the correct view)
