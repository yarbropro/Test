from django.shortcuts import render

# Create your views here.

def show_indicators(request):
    return render(request, "BestIndicators/site.html")