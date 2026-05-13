from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


@login_required
def index(request):
    template = loader.get_template("templates/index.html")
    return HttpResponse(template.render())
