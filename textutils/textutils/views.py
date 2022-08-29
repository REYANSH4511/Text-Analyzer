# I Have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def analyze(request):
    djtext=request.POST.get("text" , "default")
    removepunc=request.POST.get("removepunc" , "off")
    fullcaps=request.POST.get("fullcaps" , "off")
    removenewline=request.POST.get("removenewline" , "off")
    extraspaceremover=request.POST.get("extraspaceremover" , "off")
    charcount=request.POST.get("charcount" , "off")
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps== "on":
        analyzed = ""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if removenewline == "on":
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed+=char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Character Present ', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps != "on" and removenewline != "on" and extraspaceremover != "on" and charcount != "on"):
        return render(request,'error.html')
    return render(request, 'analyze.html', params)

