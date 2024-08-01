from typing import Any
from django.core.management.base import BaseCommand

from subscriptions.models import Subscriptions


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("hello world")
        qs = Subscriptions.objects.filter(active=True)
        for obj in qs:
          sub_perms = obj.get_permissions()
          for group in obj.get_groups():
              group.permissions.set(sub_perms)
        # subscription = Subscription.objects.create(
        #     name='Pro',
        #     description='Pro Plan',
        #     price=29.99,
        #     duration=30
        # )
        # self.stdout.write(self.style.SUCCESS(f'Subscription created: {subscription.name}'))
