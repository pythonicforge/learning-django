# This file was not created by Django but by Hardik Jaiswal
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    citations = {'author': 'Hardik Jaiswal'}
    return render(request, 'index.html', citations)

def remove_punctuation(request):
    text = request.GET.get('text', '')
    return render(request, 'remove_punctuation.html', {'analyzedText': text})

def capitalize_first(request):
    return render(request, 'capitalize_first.html')

def newline_remover(request):
    return render(request, 'newline_remover.html')

def space_remover(request):
    return render(request, 'space_remover.html')

def char_count(request):
    return render(request, 'char_count.html')