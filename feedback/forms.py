from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name",max_length=7,min_length=2)
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}))
    rating = forms.IntegerField(max_value=5,min_value=1)