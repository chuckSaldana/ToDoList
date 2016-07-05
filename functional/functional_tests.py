import unittest
from selenium import webdriver

class NewVisitorTEst(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Edith has heard about this cool new to-do lists app.
        # She goes to its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: buy a peacock feathers" as an item in a to-do list

        # There's still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly-fishing" (she is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees 
        # that the site has generated a nique URL for her -- there is some
        # explanatorytext to that effect.

        # She visits that USL - her to-do list is still there

        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main()
