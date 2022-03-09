from django.contrib import admin

# Register your models here.
from .models import Them
from .models import Question
from .models import AnswerOptions

class ChoiceInline(admin.TabularInline):
    model = AnswerOptions
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)



class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class ThemAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Them, ThemAdmin)


admin.site.register(AnswerOptions)