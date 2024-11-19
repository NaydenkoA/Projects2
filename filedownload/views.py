from django.shortcuts import render
from .models import Libr

def lib(request):
    if request.POST:
        Libr.objects.create(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            file = request.FILES.get('file')
        )
    books = Libr.objects.order_by('title')
    return render(request,'main/bib.html',{'books': books})
