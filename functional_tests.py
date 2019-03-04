"""
Functional tests are also called (End to end, acceptance or black box tests)
These tests are from the perspective of a User and do not generally care about 
the implementation.
They are used to drive User flows.
"""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        # Test if title is correct
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test !")
        
        # Comments will specify tests for the required behaviour
        
        # Enter a todo item
        
        # Type "Buy peacock feathers" into a text box
        
        # Hit Enter, "1: Buy peacock feathers" appears as an ToDo item in the list
        
        # A visible text box to enter more todo items, Enter another todo item
        # "Make a fly"
        
        # Page updates again to show both items in the list
        
        # Enable persistence and show URL and info
        
        # Visit given URL and list must exist there
        
if __name__ == "__main__":
    unittest.main(warnings="ignore")

