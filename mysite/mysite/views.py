# This file was not created by Django but by Hardik Jaiswal
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    citations = {'author': 'Hardik Jaiswal'}
    return render(request, 'index.html', citations)

def analyse_text(request):
    text = request.GET.get('text', '')
    operation = request.GET.get('operation', 'off')

    if operation == 'removepunc':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        text = analyzed
    if operation == 'capitalize':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()
        text = analyzed
    if operation == 'newlineremover':
        analyzed = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        text = analyzed
    if operation == 'spaceremover':
        analyzed = ''
        for index, char in enumerate(text):
            if not (text[index] == ' ' and text[index+1] == ' '):
                analyzed = analyzed + char
        text = analyzed
    if operation == 'charcount':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char
        text = len(analyzed)

    purpose = ""
    if operation == 'removepunc':
        purpose = "Removed Punctuations"
    if operation == 'capitalize':
        purpose = "Capitalized Text"
    if operation == 'newlineremover':
        purpose = "Removed New Lines"
    if operation == 'spaceremover':
        purpose = "Removed Extra Spaces"
    if operation == 'charcount':
        purpose = "Counted Characters"

    return render(request, 'analyse_text.html', {'analyzedText': text, 'purpose': purpose})