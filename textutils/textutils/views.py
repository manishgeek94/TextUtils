#This is main view file where we write our logic

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    value = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase','off')
    lowercase = request.POST.get('lowercase','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcount = request.POST.get('charcount','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if (uppercase == "on" and removepunc == "on" and charcount == "on"):
        analyzed =''
        for char in value:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
                count = len(analyzed)
        params = {'purpose': 'removed punctuation and upper it', 'analyzed_text': analyzed, 'charcount':count}
        return render(request, 'analyze.html', params)
# we can use elif way also for 2 -3 module but for more it will be complex
    # elif (removepunc == "on" and lowercase == "on" and charcount == "on"):
    if (removepunc == "on" and lowercase == "on" and charcount == "on"):
        count = ''
        analyzed = ''
        for char in value:
            if char not in punctuations:
                analyzed = analyzed + char.lower()
                count = len(analyzed)
        params = {'purpose':'Removed punctuations and lower it','analyzed_text':analyzed,'charcount':count}
        value = analyzed
        # return render(request,'analyze.html',params)
    if removepunc == "on":
        analyzed = ''
        for char in value:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        value = analyzed
        # return render(request,'analyze.html',params)
    if(uppercase == "on"):
        analyzed = ''
        for char in value:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'to uppercase now', 'analyzed_text': analyzed}
        value = analyzed
        # return render(request, 'analyze.html', params)
    if(lowercase == 'on'):
        analyzed = ''
        for char in value:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'to uppercase now', 'analyzed_text': analyzed}
        value = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremove == 'on'):
        analyzed = ''
        for char in value:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        value = analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremove == 'on'):
        analyzed = ''
        for index, char in enumerate(value):
            if not (value[index] == " " and value[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'remove extra space line', 'analyzed_text': analyzed}
        value = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == 'on'):
        analyzed = len(value)
        params = {'purpose': 'Char counter calculater', 'charcount': analyzed}
        value = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and uppercase != "on" and lowercase != 'on' and newlineremove != 'on' and extraspaceremove != 'on' and charcount != 'on'):
        return HttpResponse("error")

    return render(request, 'analyze.html', params)
