from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def feedback_index(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/done')

    return render(request, 'feedback.html')

def done(request): 

    return render(request, 'done.html')


    