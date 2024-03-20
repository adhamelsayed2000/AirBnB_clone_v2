#!/usr/bin/python3

import unittest
import MySQLdb
from console import HBNBCommand
import io
import sys

class TestCreateState(unittest.TestCase):
    def setUp(self):
        # Connect to the test database
        self.db = MySQLdb.connect(user='your_username', passwd='your_password', db='test_database')
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Clean up resources
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        # Get initial count of records in the states table
        self.cursor.execute('SELECT COUNT(*) FROM states')
        initial_count = self.cursor.fetchone()[0]

        # Redirect stdout to capture console output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Execute the command in the console
        HBNBCommand().onecmd('create State name="California"')

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Get count of records after executing the command
        self.cursor.execute('SELECT COUNT(*) FROM states')
        final_count = self.cursor.fetchone()[0]

        # Compare counts and assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()
