# This file was not created by Django but by Hardik Jaiswal
from django.http import HttpResponse


def home(request):
    return HttpResponse('''<h2>Welcome to Text-Utils</h2>
    <p>Perform various operations on text</p>
    <ul>
    <li><a href="/remove-punctuation/">Remove Punctuation</a></li>
    <li><a href="/capitalize-first/">Capitalize First</a></li>
    <li><a href="/newline-remover/">Remove NewLines</a></li>
    <li><a href="/space-remover/">Remove Spaces</a></li>
    <li><a href="/char-count/">Count Number of Characters</a></li>
    </ul>
    ''')

def remove_punctuation(request):
    return HttpResponse('''<h2>Remove All Punctuations</h2>
    <a href="/">Go Back</a>
    ''')

def capitalize_first(request):
    return HttpResponse('''<h2>Capitalize First Letter</h2>
    <a href="/">Go Back</a>
    ''')

def newline_remover(request):
    return HttpResponse('''<h2>Remove All NewLines</h2>
    <a href="/">Go Back</a>
    ''')

def space_remover(request):
    return HttpResponse('''<h2>Remove All Spaces</h2>
    <a href="/">Go Back</a>
    ''')

def char_count(request):
    return HttpResponse('''<h2>Count Number of Characters</h2>
    <a href="/">Go Back</a>
    ''')