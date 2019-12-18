from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TestForm
from .models import TestModel


# Create your views here.
def index(request):
    if request.method == "POST":
        returnedForm = TestForm(request.POST)
        if returnedForm.is_valid():
            returnedForm.save()
        # return HttpResponseRedirect("/")
    return render(request, 'crudApp/index.html',
                  {"form": TestForm(),
                   "allInfo": TestModel.objects.all()
                   })

def edit(request, testID):
    if request.method == 'POST':
        tempModel = TestModel.objects.get(pk=testID)
        form = TestForm(request.POST, instance=tempModel)
        form.save()
        return HttpResponseRedirect("/")
    else:
        tempModel = TestModel.objects.get(pk=testID)
        form = TestForm(instance=tempModel)
        return render(request, 'crudApp/index.html',{"form": form})

def delete(request, testID):
    tempModel = TestModel.objects.get(pk=testID)
    tempModel.delete()
    return HttpResponseRedirect("/")