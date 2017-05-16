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
    import numpy as np
    stocks = np.loadtxt('/upload/simple-file-upload/uploads/core/foo.txt')

    stock0 = np.array([])
    stock1 = np.array([])
    stock2 = np.array([])
    stock3 = np.array([])
    stock4 = np.array([])
    stock5 = np.array([])
    stock6 = np.array([])
    stock7 = np.array([])
    stock8 = np.array([])


    for i in range(stock[2].shape[0]):
        if stock[2][i]==7:
            stock0 = np.append(stock0,int(stock[3][i]))
            
        elif stock[2][i]==6:
            stock1 = np.append(stock1,int(stock[3][i]))
        
        elif stock[2][i]==5:
            stock2 = np.append(stock1,int(stock[3][i]))
            
        elif stock[2][i]==4:
            stock3 = np.append(stock1,int(stock[3][i]))
            
        elif stock[2][i]==3:
            stock4 = np.append(stock1,int(stock[3][i]))
            
        elif stock[2][i]==2:
            stock5 = np.append(stock1,int(stock[3][i]))
            
        elif stock[2][i]==1:
            stock6 = np.append(stock1,int(stock[3][i]))
            
        elif stock[2][i]==0:
            stock7 = np.append(stock1,int(stock[3][i]))
            
        else :
            stock8 = np.append(stock1,int(stock[3][i]))

    stocks = np.array([stock0,stock1,stock2,stock3,stock4,stock5,stock6,stock7,stock8])        
    return render(request,'core/predict_sotck.html',{
        'stocks':stocks
        })

def model_desc(request):
    return render(request, 'core/Model_desc.html')

def lotter_desc(request):
    return render(request, 'core/Lottery_test.html')