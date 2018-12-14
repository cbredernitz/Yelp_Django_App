from django.contrib import admin
import yelp.models as models


@admin.register(models.Attire)
class AttireAdmin(admin.ModelAdmin):
	fields = [
		'attire'
	]

	list_display = [
		'attire'
	]

	list_filter = ['attire']

# admin.site.register(models.Attire)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	fields = [
		'user_name',
        'review_count',
        'average_stars',
        'yelper_since'
	]

	list_display = [
		'user_name',
        'review_count',
        'average_stars',
        'yelper_since'
	]
