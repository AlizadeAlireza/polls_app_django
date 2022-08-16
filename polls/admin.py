from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #the number of choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                ("Question Information",             {'fields' : ['question_text']}),
                ('Date information', {'fields' : ['pub_date']}),
        ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(Choice)
