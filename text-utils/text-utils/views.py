from django.shortcuts import render

def home(request):
    citations = {'author': 'Hardik Jaiswal'}
    return render(request, 'index.html', citations)

def analyse_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        operations = request.POST.getlist('operation', [])
        analyzed = text

        if 'removepunc' in operations:
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ''.join(char for char in analyzed if char not in punctuations)

        if 'capitalize' in operations:
            analyzed = analyzed.upper()

        if 'newlineremover' in operations:
            analyzed = analyzed.replace('\n', '').replace('\r', '')

        if 'spaceremover' in operations:
            analyzed = ' '.join(analyzed.split())

        purposes = []
        if 'removepunc' in operations:
            purposes.append("Removed Punctuations")
        if 'capitalize' in operations:
            purposes.append("Capitalized Text")
        if 'newlineremover' in operations:
            purposes.append("Removed New Lines")
        if 'spaceremover' in operations:
            purposes.append("Removed Extra Spaces")

        purpose = " and ".join(purposes) if purposes else "No Operation Performed"
        
        return render(request, 'analyse_text.html', {'analyzedText': analyzed, 'purpose': purpose})
