from django.forms import ModelForm
from django.forms import fields
from .models import Code, Comment, Language

class CodeSubmissionForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CodeSubmissionForm, self).__init__(*args, **kwargs)
        
        language = Language.objects.order_by('-is_popular', 'name').all()

        self.fields['language'].choices = [[lang.pk, lang.name] for lang in language]

    class Meta:
        model = Code
        fields = '__all__'
        exclude = ['total_views', 'author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']