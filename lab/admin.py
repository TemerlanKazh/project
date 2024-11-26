from django.contrib import admin
from .models import Cars,Review,Game,Subscriptions,gadgets


class ReviewAdmin(admin.ModelAdmin):
    # определение отображаемых полей в админке, если необходимо
    list_display = ['user', 'rev']
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cars)
admin.site.register(Game)
admin.site.register(Subscriptions)
admin.site.register(gadgets)
