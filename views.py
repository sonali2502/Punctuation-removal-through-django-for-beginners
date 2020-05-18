# I have created this file- Sonali Sharma
# creating http response because views return http response.
from django.http import HttpResponse
from django.shortcuts import render # for templates

# for pipelining
# Pipeline is an asset packaging library for Django, providing both CSS and JavaScript concatenation and compression, built-in JavaScript template support, and optional data-URI image and font embedding
def index(request):
    params = {'name':'Sonali','place':'Mars'}
    return render (request,'index.html',params) # requesting to run index.html
    # third arg is also present, i.e, a variable, i.e you can pass dictionary 
   # return HttpResponse("<h2>Home</h2>")



def analyze(request):
 
    djtext = request.GET.get('text', 'default') # displays text , if not presesnt will dispaly default

    # Check checkbox values
    rempunctuations = request.GET.get('rempunctuations', 'off')
    print(rempunctuations)
    #Check which checkbox is on
    if rempunctuations == "on":
        punctuations = '''!()-[]{};:,'"\\<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
 


# Templating - Creating html files separately
# step-1 go to settings.py , add templates to DIRS[]
# step 2 create dir templates, add index.html

