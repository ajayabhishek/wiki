from django.forms import ModelForm
from .models import Article
from .models import category
from django.forms import CharField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class NameForm(ModelForm):
    class Meta:
        model = Article
        fields = ['cat_id', 'title', 'content']
