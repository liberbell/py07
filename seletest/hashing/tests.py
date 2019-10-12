from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        # assert browser.page_source.find('install')
        # self.assertIn('install', self.browser.page_source)
        self.assertIn('Enter hash here', self.browser.page_source)

    def tesh_hash_of_hello(self):
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()
