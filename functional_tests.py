from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # app want user to add a new todo
        input_box=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        
        # user type buy peacock fethers
        input_box.send_keys('Buy peacock feathers')

        # after user press Enter button, he could see the todo item in table
        input_box.send_keys(Keys.ENTER)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


        self.fail('Finish the test')

if __name__ =="__main__":
    unittest.main()
