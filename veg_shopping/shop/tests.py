from django.test import LiveServerTestCase

# Create your tests here.

from django.contrib.auth.models import User
from selenium import webdriver

class AdminTest(LiveServerTestCase):
    def setUp(self):
        User.objects.create_superuser(username="test_admin",password="test_admin_password",email="")
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTest,self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(AdminTest, self).tearDown()



