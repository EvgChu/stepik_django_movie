from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from .forms import FeedbackForm
from .models import FeedbackModel

def feedback_index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('feedback-done')
            return HttpResponseRedirect(url)
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', context={
        "form": form
    })

def update_feedback(request, id_feedback):
    feed = get_object_or_404(FeedbackModel,id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            url = reverse('feedback-done')
            return HttpResponseRedirect(url)
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback.html', context={
        "form": form
    })

def done(request): 

    return render(request, 'done.html')


    