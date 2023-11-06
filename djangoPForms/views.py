from django.shortcuts import render
from djangoPForms.forms import HpStudentsForm


def home(request):
    stud = HpStudentsForm()
    return render(request, 'index.html', {'form': stud})
