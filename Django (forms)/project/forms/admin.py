from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3  # Yeni soru eklediğinizde varsayılan 2 cevap ekler

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]  # Cevapları soru formunda göster

admin.site.register(Question, QuestionAdmin)  # Question modelini admin paneline kaydeder
