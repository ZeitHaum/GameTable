from django.shortcuts import render

# Create your views here.
def goToGameTable(request):
    return render(request,"GameTable.html")
