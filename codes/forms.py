from django.forms import ModelForm
from django.forms import fields
from .models import Code, Language

class CodeSubmissionForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CodeSubmissionForm, self).__init__(*args, **kwargs)
        
        language = Language.objects.order_by('-is_popular', 'name').all()

        self.fields['language'].choices = [[lang.language_code, lang.name] for lang in language]

    class Meta:
        model = Code
        fields = '__all__'
        exclude = ['total_views', 'author']