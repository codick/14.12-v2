from django import forms

class UserForm(forms.Form):
    title = forms.CharField()
    URL = forms.URLField()
    content = forms.CharField(widget=forms.Textarea)
    checkbox = forms.BooleanField()
    choice = forms.ChoiceField(choices=((1, 'Еда'), (2, 'Новости'), (3, 'Спорт')))
