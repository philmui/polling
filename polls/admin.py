from django.contrib import admin

from .models import Choice, Question

admin.AdminSite.site_header = "Polling Administration"

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['text']
	fieldsets = [
		(None,               {'fields': ['text']}),
		('Date information', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
