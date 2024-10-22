from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyModelForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('filtering')
    else:
        form = MyModelForm()
    return render(request, 'image_upload.html', {'form': form})


def filtering(request):
    return HttpResponse("This is the filtering page")
