from django.shortcuts import render

# Create your views here.
def listSession(request):
    context = {}
    return render(request, "session/list_sessions.html", context)