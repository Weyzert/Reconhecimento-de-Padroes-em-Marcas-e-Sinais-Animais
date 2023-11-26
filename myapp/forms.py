from django import forms
from .models import ImageResult

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageResult
        fields = ['image']
