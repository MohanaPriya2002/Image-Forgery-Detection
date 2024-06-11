from django import forms
from .models import Chat_details


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Chat_details
        fields = ('ContextImage',) 

