from django.conf import settings
from django.core.management.base import BaseCommand
# from authentication.models import Account
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = 'root'
        email = 'root@mail.ru'
        password = '123'
        User.objects.create_superuser(username, email, password)
