from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')