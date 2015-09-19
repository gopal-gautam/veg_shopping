from django.test import TestCase, LiveServerTestCase

# Create your tests here.
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from customer.models import Customer
from customer.forms import LoginForm
from customer.forms import RegistrationForm
from selenium import webdriver


class CustomerTest(TestCase):
    def create_customer(self, name="test name", username="test_name", password="test_password"):
        return Customer.objects.create(name=name, username=username, password=password)


    def test_customer_creation(self):
        c = self.create_customer()
        self.assertTrue(isinstance(c,Customer))


class SeleniumBaseTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(SeleniumBaseTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumBaseTest, self).tearDown()

    def open(self, url):
        self.selenium.get("%s%s" % (self.live_server_url, url))

    def elem_css(self, css_selector):
        """
        a shortcut function to select the element matching the specified css selector
        :param css_selector:
        :return:
        """
        element = self.selenium.find_elements_by_css_selector(css_selector)
        elementLength = len(element)
        if elementLength == 1:
            return element[0]

        elif not element:
            raise NoSuchElementException(css_selector)

        return element

    def wait_for_css(self, css_selector, timeout=7):
        """ Shortcut for WebDriverWait"""
        return WebDriverWait(self, timeout).until(lambda driver : driver.find_css(css_selector))


class SeleniumTest(SeleniumBaseTest):
    def test_selenium_automation(self):
        """
        Perform a new selenium browser automation test
        :return:
        """
        #create a test customer
        test_name = "test name"
        test_username = "test_username"
        test_password = "test_password"
        self.open('/customer/register')
        name= self.elem_css('#id_name')
        name.send_keys(test_name)
        username = self.elem_css('#id_username')
        username.send_keys(test_username)
        password = self.elem_css('#id_password')
        password.send_keys(test_password)
        register = self.selenium.find_element_by_xpath('//input[@value="register"]')
        register.click()

        #create the test farmer
        test_farmer_name = 'test farmer'
        test_farmer_username = 'test_farmer_username'
        test_farmer_password = 'test_farmer_password'
        self.open('/farmer/register')
        self.elem_css('#id_name').send_keys(test_farmer_name)
        self.elem_css('#id_username').send_keys(test_farmer_username)
        self.elem_css('#id_password').send_keys(test_farmer_password)
        self.selenium.find_element_by_xpath('//input[@value="register"]').click()

        #test the login of newly created farmer
        self.open('/farmer/login')
        self.elem_css('#id_username').send_keys(test_farmer_username)
        self.elem_css('#id_password').send_keys(test_farmer_password)
        self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        self.assertIn(test_farmer_name,self.selenium.page_source)

        #test adding new tarkari to godam
        test_tarkari_name = "test_tarkari_name"
        test_tarkari_price = "20"
        test_tarkari_expiry_day = "3"
        test_tarkari_quant = "30"
        self.open('/farmer/farmer_portal')
        self.selenium.find_element_by_xpath('//input[@name="tarkari_name"]').send_keys(test_tarkari_name)
        self.selenium.find_element_by_xpath('//input[@name="tarkari_price"]').send_keys(test_tarkari_price)
        self.selenium.find_element_by_xpath('//input[@name="tarkari_expiry_day"]').send_keys(test_tarkari_expiry_day)
        self.selenium.find_element_by_xpath('//input[@name="tarkari_quant"]').send_keys(test_tarkari_quant)
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_xpath('//input[@value="Add Tarkari"]').click()
        self.open('/farmer/farmer_portal')
        self.selenium.implicitly_wait(10)
        self.assertIn(test_tarkari_name, self.selenium.page_source)
        self.assertIn(test_tarkari_price, self.selenium.page_source)
        self.assertIn(test_tarkari_quant, self.selenium.page_source)
        self.assertIn(test_tarkari_expiry_day, self.selenium.page_source)

        #Now test the login with newly created login
        self.open('/customer/login')
        username = self.elem_css('#id_username')
        username.send_keys(test_username)
        password = self.elem_css('#id_password')
        password.send_keys(test_password)
        self.selenium.find_element_by_xpath('//input[@value="submit"]').click()
        self.assertIn(test_name,self.selenium.page_source)

        #Now test adding some items to the carts
        self.open('/listTarkari')
        self.selenium.implicitly_wait(10)
        self.assertIn(test_name, self.selenium.page_source)
        inputs = self.selenium.find_elements_by_tag_name("input")
        for input in inputs:
            id = input.get_attribute("id")
            tarkari_id = str(id).split("_")[1]
            print "test: tarkari id is %s" % tarkari_id
            self.open('/addCart/%s/%s' % (tarkari_id,2))
            self.assertNotIn("Invalid Tarkari Defined",self.selenium.page_source)
            self.assertNotIn("We don't have that much tarkari available is",self.selenium.page_source)
            self.selenium.save_screenshot('screenshot_list_tarkari.png')

        #Now test committing the buy
        self.open('/buy')

        #view the reports
        self.open('/report')
        self.selenium.start_client()
        self.selenium.save_screenshot('screenshot_total_report.png')


