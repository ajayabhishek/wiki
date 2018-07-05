from django.contrib import admin
from .models import category
from .models import Article
from .models import Document


admin.site.register(category)
admin.site.register(Article)
admin.site.register(Document)


# Register your models here.
