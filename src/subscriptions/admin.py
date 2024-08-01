from django.contrib import admin

from .models import Subscriptions, UserSubscriptions, SubscriptionsPrice


class SubscriptionPrice(admin.StackedInline):
    model = SubscriptionsPrice
    can_delete = False
    readonly_fields = ['stripe_id']
    extra = 0


class SubscriptionsAdmin(admin.ModelAdmin):
    inlines = [SubscriptionPrice]
    list_display = ('name', 'active')
    readonly_fields = ['stripe_id']


admin.site.register(Subscriptions, SubscriptionsAdmin)
admin.site.register(UserSubscriptions)
