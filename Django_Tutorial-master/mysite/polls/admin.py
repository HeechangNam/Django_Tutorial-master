from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
	
    fieldsets = [ (None, {'fields':['question_text']}), ('Date information', {'fields':['pub_date'], 'classes' : ['collapse']}),]
    inlines = [ChoiceInline]
	
    list_filter = ['pub_date']
    search_fields = ['question_text']
	#fields = ['pub_date', 'question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
