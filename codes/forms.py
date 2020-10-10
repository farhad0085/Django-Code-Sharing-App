from django.forms import ModelForm
from django.forms import fields
from .models import Code

class CodeSubmissionForm(ModelForm):
    class Meta:
        model = Code
        fields = '__all__'
        exclude = ['total_views', 'author']