from django import forms

class ContactMe(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern' : '-?[0-9]*(\.[0-9]+)?'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'mdl-textfield__input'}))