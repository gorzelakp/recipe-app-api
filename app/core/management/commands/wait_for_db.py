import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django pauzuje wykonanie dopóki baza nie bedzie dostępna"""
    
    def handle(self, *args, **options):
        self.stdout.write('Czekamy na baze')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Baza niedostepna, czekamy')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('BAZA DOSTEPNA SMIECIU'))
        
    