from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

browser.get('http://localhost:8000')

assert browser.page_source.find('install')
