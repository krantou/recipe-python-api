"""
Test custom management commands.
"""

from unittest.mock import patch

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

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting Operational error"""
        patched_check.side_effect = [Psycoppg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(database=['default'])