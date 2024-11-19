from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def dop(request):
    return render(request, 'main/dop.html')

def dop1(request):
    return render(request, 'main/dop1.html')


