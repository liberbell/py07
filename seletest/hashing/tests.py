from django.test import TestCase
from selenium import webdriver

# Create your tests here.
browser = webdriver.Safari()
browser.get('http://localhost:8000')

assert browser.page_source.find('install')
