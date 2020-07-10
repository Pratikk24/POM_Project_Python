import unittest
import HtmlTestRunner
from Locators.locators import Locators
from Tests.admin_user_test_cases import Admin_user_login
from Tests.qc_user_test_cases import QC_user_login


# get all test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(Admin_user_login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(QC_user_login)

# creating test suites
admin = unittest.TestSuite(tc1)
qc = unittest.TestSuite(tc2)
master = unittest.TestSuite([tc1, tc2])

# run tests
#suit = unittest.TextTestRunner(verbosity=2).run(qc)

html_runner = HtmlTestRunner.HTMLTestRunner(Locators.output, combine_reports=True)
html_runner.run(master)
