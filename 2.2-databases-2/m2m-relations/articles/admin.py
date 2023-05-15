from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data:
                main_count += int(form.cleaned_data['is_main'])
        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_count > 1:
            raise ValidationError('Допускается только один основной раздел')
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', ]
    list_filter = ['title', 'published_at', ]
    inlines = [ScopeInLine, ]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
