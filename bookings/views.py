from django.shortcuts import render

from django.http import HttpResponse


def startseite(request):
    return HttpResponse("Terminplanung der Arztpraxis funktioniert!")
