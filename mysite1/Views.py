from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    p={'name':'rahul','age':25}
    return render(request,'index.html',p)


def Analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline_remover=request.POST.get('newline_remover','off')
    char_count=request.POST.get('char_count','off')

    # 1ST code for punctuation removing
    if removepunc=="on":
        analysed=""
        puntuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in puntuations:
                analysed=analysed+char
        pa={'purpose':'remove punctuation','analysed_text':analysed}
        djtext=analysed

    #2ND code for convert whole string into UPPERCASE
    if fullcaps == "on":
        analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        pa = {'purpose': 'UPPER CASE', 'analysed_text': analysed}
        djtext=analysed

    # 3RD CODE FOR NEWLINE REMOVER
    if newline_remover=='on':
        analysed=""
        for char in djtext:
            if char!='\n':
                analysed=analysed+char
        pa = {'purpose': 'NewLine Remover', 'analysed_text': analysed}
        djtext=analysed

    #4TH CODE FOR SPACE REMOVER
    if char_count=="on":
        all_freq = {}

        for i in djtext:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1

        pa={'purpose':'space remover','analysed_text':all_freq}
        djtext=analysed

    if (removepunc!="on" and fullcaps !="on" and newline_remover!='on' and char_count!="on" ):
        return HttpResponse("You did not select any checkbox please select atleast one checkbox to remove this error")

    return render(request, 'analysed.html', pa)
