from django.core.management.base import BaseCommand
from ...source import eternalUpdatenewsLoop

class Command(BaseCommand):
    help = 'Тестирование'

    def handle(self, *args, **kwargs):
        eternalUpdatenewsLoop()
