from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class ChoiceInline(admin.StackedInline):
    model = Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade_pt')
    list_filter = ['course__name', 'grade_pt', 'question_text', 'course__pub_date', 'course__total_enrollment']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choices', 'is_correct')
    list_filter = ['question', 'question__course__name', 'is_correct', 'question__question_text']
    search_fields = ['is_correct', 'question__course__name', 'question__question_text']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
