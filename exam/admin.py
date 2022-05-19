from django.contrib import admin

from exam.models import Exam, ExamSet, Question

# Register your models here.


class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'duration',
        'totalMarks',
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )


class ExamSetAdmin(admin.ModelAdmin):
    list_display = (
        'exam',
        'user',
    )


admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(ExamSet)
