
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'index.html')

def count(request):

    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddick = {}

    for word in wordlist:
        if word in worddick:
            # increament its key value
            worddick[word] += 1
        else:
            worddick[word] = 1

    words = sorted(worddick.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'text':fulltext, 'fulltext':words, 'count':len(words)})




def about(request):
    return render(request, 'about.html', {'Rohit':'Rohit'})
