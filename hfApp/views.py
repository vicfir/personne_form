from django.shortcuts import render, redirect
from .models import Personne
from .forms import PersonneForm

# Create your views here.
def home(request):
    data = Personne.objects.all()
    # plus24 = Personne.objects.filter(age__gte= 24)
    filles = Personne.objects.filter(genre= 'femme')
    garcon = Personne.objects.filter(genre= 'homme')

    if request.method == 'POST' :
        form = PersonneForm(request.POST)
        if form.is_valid():
            personne = form.save()
            return redirect('home')
    else :
        form = PersonneForm()

    context = {
        'personnes' : data,
        'femmes' : filles,
        'hommes' : garcon,
        'form':form
    }
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST' :
        form = PersonneForm(request.POST)
        if form.is_valid():
            personne = form.save()
            return redirect('home')
    else :
        form = PersonneForm()
    return render(request, 'add_persone.html', {'form':form})