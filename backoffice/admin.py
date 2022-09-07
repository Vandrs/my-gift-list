from django.contrib import admin
from core.models import Event, GiftList, Gift


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("event_name", )}
    fields = ('event_name', 'event_date', 'holder_name', 'event_location', 'slug', 'is_active')
    list_display = ('event_name', 'event_date', 'created_at')


class GiftListAdmin(admin.ModelAdmin):
    pass


class GiftAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(GiftList, GiftListAdmin)
admin.site.register(Gift, GiftAdmin)
