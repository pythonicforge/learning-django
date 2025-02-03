# This file was not created by Django but by Hardik Jaiswal
from django.http import HttpResponse


def home(request):
    return HttpResponse('''<h2>Home Page</h2>
    <p>This is the home page</p>
    <ul>
    <li><a href="/about/">About</a></li>
    <li><a href="/projects/">Projects</a></li>
    </ul>
    ''')

def about(request):
    return HttpResponse('''<h2>About Page</h2>
    <p>This is the about page</p>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/projects/">Projects</a></li>
    </ul>
    ''')

def projects(request):
    return HttpResponse('''<h2>Projects Page</h2>
    <p>This is the projects page</p>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    </ul>
    ''')