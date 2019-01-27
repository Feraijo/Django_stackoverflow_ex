from django.contrib import admin

from .models import Answer, Question


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date', 'has_answer']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['has_answer']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [AnswerInline]
    list_display = ('question_text', 'has_answer','pub_date')

admin.site.register(Question, QuestionAdmin)