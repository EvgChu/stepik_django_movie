from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from .forms import FeedbackForm

def feedback_index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            
            url = reverse('feedback-done')
            return HttpResponseRedirect(url)

    return render(request, 'feedback.html', context={
        "form": form
    })

def done(request): 

    return render(request, 'done.html')


    