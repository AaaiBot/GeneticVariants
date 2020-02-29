import unittest

from predicting_cancer_variants.src.common_tests.configuration_unit_tests import ConfigurationUnitTests
from predicting_cancer_variants.src.download_mutation_data_tests.create_database_tests.create_database_controller_system_tests \
    import CreateDatabaseControllerSystemTests
from predicting_cancer_variants.src.download_mutation_data_tests.create_database_tests.table_unit_tests import \
    TableUnitTests
from predicting_cancer_variants.src.download_mutation_data_tests.fetch_cbioportal_data_tests.download_controller_system_tests \
    import DownloadControllerSystemTests


def create_suite():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromTestCase(ConfigurationUnitTests))
    suite.addTests(loader.loadTestsFromTestCase(TableUnitTests))
    suite.addTests(loader.loadTestsFromTestCase(CreateDatabaseControllerSystemTests))
    suite.addTests(loader.loadTestsFromTestCase(DownloadControllerSystemTests))

    return suite


if __name__ == '__main__':
    # get a fully loaded test suite
    test_suite = create_suite()

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(test_suite)
