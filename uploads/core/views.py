from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def lotter_main_page(request):
    return render(request, 'core/lotter_main_page.html')


def lotter_extractor(request):
    import sys
    sys.path.append('/upload/simple-file-upload')
    
    import lottery as lt
    import numpy as np
    datatxt = np.loadtxt('/upload/simple-file-upload/uploads/core/data.txt')
    hello = lt.Lottery(datatxt)
    hello.MLL(23)
    hello.Test()
    form = hello.returnLotterynum()[1]
    return render(request, 'core/lotter_extractor.html',{
        'form':form
    })

def predict_stock(request):
    return render(request,'core/predict_sotck.html')

def model_desc(request):
    return render(request, 'core/Model_desc.html')

def lotter_desc(request):
    return render(request, 'core/Lotter_test.html')