from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from .forms import FeedbackForm
from .models import FeedbackModel

def feedback_index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = FeedbackModel(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating']
            )
            feed.save()
            url = reverse('feedback-done')
            return HttpResponseRedirect(url)

    return render(request, 'feedback.html', context={
        "form": form
    })

def done(request): 

    return render(request, 'done.html')


    