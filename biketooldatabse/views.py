from django.shortcuts import render


def layout(request):
    return render(request, "database/layout.html", )