"""
Functional tests are also called (End to end, acceptance or black box tests)
These tests are from the perspective of a User and do not generally care about 
the implementation.
They are used to drive User flows.
"""
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        # Test if title is correct
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # Comments will specify tests for the required behaviour
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        
        # Type "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")
        
        # Hit Enter, "1: Buy peacock feathers" appears as an ToDo item in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy Peacock Feathers' for row in rows)
        )
        
        # A visible text box to enter more todo items, Enter another todo item
        # "Make a fly"
        self.fail("Finish tests")

        
        # Page updates again to show both items in the list
        
        # Enable persistence and show URL and info
        
        # Visit given URL and list must exist there
        
        self.fail("Finish the test !")

if __name__ == "__main__":
    unittest.main(warnings="ignore")

