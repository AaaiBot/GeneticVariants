import os
import sqlite3
import unittest

from predicting_cancer_variants.src.common import configuration
from predicting_cancer_variants.src.common.configuration import Configuration
from predicting_cancer_variants.src.download_mutation_data import create_database_controller, download_controller


class DownloadControllerSystemTests(unittest.TestCase):

    __test_configuration_file = r"Test Configuration Files\create_database_test_configuration.yaml"

    # run once, before any test scenarios start to run
    @classmethod
    def setUpClass(cls):
        # Clean up before running each test, in case quited test before tearDown() was run, eg when debugging
        cls.__cleanup()

        # Use test YAML configuration file
        Configuration(cls.__test_configuration_file)

        # Delete test database if it exists
        if os.path.exists(Configuration().database_location):
            os.remove(Configuration().database_location)

        # Create the database
        create_database_controller.run()

        # populate the database
        download_controller.run()

    # run once, after all test scenarios have run
    @classmethod
    def tearDownClass(cls):
        # Clean up after running each test
        cls.__cleanup()

    @staticmethod
    def __cleanup():
        # Prevent singleton Configuration object hanging on from a previous test, or accidentally used in the future
        configuration.reset_singleton()

    def test_database_file_exists(self):
        # Database should now exist
        self.assertTrue(os.path.exists(Configuration().database_location))

    def test_cancer_table_is_populated(self):
        # Connect to the database, and get a count of the number of rows in the cancer table
        db = sqlite3.connect(Configuration().database_location)
        cursor = db.cursor()
        results = cursor.execute("SELECT COUNT(*) FROM test_cancers;")
        value = results.fetchone()

        # There should be at least two rows in the table
        self.assertGreaterEqual(value[0], 2)

    def test_study_table_is_populated(self):
        # Connect to the database, and get a count of the number of rows in the studies table
        db = sqlite3.connect(Configuration().database_location)
        cursor = db.cursor()
        results = cursor.execute("SELECT COUNT(*) FROM test_studies;")
        value = results.fetchone()

        # There should be at least two rows in the table
        self.assertGreaterEqual(value[0], 2)

    def test_molecular_profiles_table_is_populated(self):
        # Connect to the database, and get a count of the number of rows in the molecular profiles table
        db = sqlite3.connect(Configuration().database_location)
        cursor = db.cursor()
        results = cursor.execute("SELECT COUNT(*) FROM test_molecular_profiles;")
        value = results.fetchone()

        # There should be at least two rows in the table
        self.assertGreaterEqual(value[0], 2)

    def test_genes_table_is_populated(self):
        # Connect to the database, and get a count of the number of rows in the genes table
        db = sqlite3.connect(Configuration().database_location)
        cursor = db.cursor()
        results = cursor.execute("SELECT COUNT(*) FROM test_genes;")
        value = results.fetchone()

        # There should be at least two rows in the table
        self.assertGreaterEqual(value[0], 2)

    def test_mutations_table_is_populated(self):
        # Connect to the database, and get a count of the number of rows in the mutations table
        db = sqlite3.connect(Configuration().database_location)
        cursor = db.cursor()
        results = cursor.execute("SELECT COUNT(*) FROM test_mutations;")
        value = results.fetchone()

        # There should be at least two rows in the table
        self.assertGreaterEqual(value[0], 2)
