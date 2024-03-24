"""
Django command to wait for db to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError 

class Command(BaseCommand):
    """Djangp command to wait for db."""

    def handle(self, *args, **options):
        """Entrypoint for command"""

        self.stdout.write('Waintg for db ...')

        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Db unavailable, waiting for 1 sec ...')

        self.stdout.write(self.style.SUCCESS('DB AVAILABLE!'))

