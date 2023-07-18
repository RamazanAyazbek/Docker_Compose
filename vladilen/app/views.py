from django.shortcuts import render, HttpResponse
from .models import List
from .forms import ListForm
def home(request):
    # form=ListForm(request.POST)
    title=request.POST.get('data')
    print(title)
    lists=List.objects.all()
    context={
        "lists":lists
    }
    return render(request, 'app/home.html', context)



    
