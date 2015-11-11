from django import forms

class ContactMe(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'padding': '100'}))
	mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'mdl-textfield__input'}))