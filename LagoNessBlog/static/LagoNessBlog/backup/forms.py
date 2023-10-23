from django import forms


class CreationForm(forms.Form):
    categories = (
        ('sports', 'Sports'),
        ('travelling', 'Travelling'),
        ('youtube', 'YouTube'),
        ('other', 'Other')
    )
    name = forms.CharField()
    category = forms.ChoiceField(choices=categories)
    description = forms.CharField()
    emailContact = forms.EmailField()
    image = forms.ImageField()
