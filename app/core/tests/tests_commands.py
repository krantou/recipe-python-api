"""
Test custom management commands.
"""

from unittest import patch

from psycopg2 import OperationalError as Psycoppg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# mock behavior: path + command.check which is provided by base command
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    
    # patched_check arg -> catches the returned value (response) from check method
    def test_wiat_for_db_ready(self, patched_check):
        """Test waiting for db  if db is ready."""

        patched_check.return_value = True
        
        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])
