from cProfile import label
from dataclasses import field
from django import forms
from .models import FeedbackModel

# class FeedbackForm(forms.Form):
#     name = forms.CharField(label="Name",max_length=7,min_length=2)
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':80}))
#     rating = forms.IntegerField(max_value=5,min_value=1)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        # fields = ['name','surname','feedback','rating']
        fields = '__all__'
        labels = {
            'name': "Имя"
        }
        error_messages = {
            'name' : {
                
            }
        }