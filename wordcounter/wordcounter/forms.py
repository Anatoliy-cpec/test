from django import forms
import os
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import CounterFile

class FileForm(forms.ModelForm):
    class Meta:
       model = CounterFile
       fields = ['file',]
       widgets = {'file': forms.FileInput,}
    
    def clean(self):
            cleaned_data = super().clean()
            file = cleaned_data.get("file")
            if file is not None:
                file = str(file)
                file_ext = os.path.splitext(file)[1]
                if file_ext != '.txt':
                        raise ValidationError({
                                "file": "Invalid format. Please use txt"
                        })


