import sys
import unittest
from selenium import webdriver
import os

from config.Config import Config
from enums import ContactPageEnums
from pages.ContactPage import ContactPage
from testdata.TestData import TestData


class ContactPageTest(unittest.TestCase):

    def setUp(self):
        driver_path = os.path.realpath('../webdrivers/chromedriver.exe')
        self.driver = webdriver.Chrome(driver_path)
        self.contact_page = ContactPage(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.data = TestData()
        self.url = Config().get_url(ENV)
        self.enums = ContactPageEnums

    def test_fill_contact_form(self):
        self.driver.get(self.url)
        self.contact_page.chose_client_type()
        self.contact_page.type_name(self.data.get_data(self.__class__.__name__,
                                                       self.enums.DataTypes.CorrectData.value,
                                                       self.enums.Data.Name.value))

        self.contact_page.type_email(self.data.get_data(self.__class__.__name__,
                                                        self.enums.DataTypes.CorrectData.value,
                                                        self.enums.Data.Email.value))

        self.contact_page.type_phone(self.data.get_data(self.__class__.__name__,
                                                        self.enums.DataTypes.CorrectData.value,
                                                        self.enums.Data.Phone.value))

        self.contact_page.chose_subject(self.data.get_data(self.__class__.__name__,
                                                           self.enums.DataTypes.CorrectData.value,
                                                           self.enums.Data.Subject.value))

        self.contact_page.type_content(self.data.get_data(self.__class__.__name__,
                                                          self.enums.DataTypes.CorrectData.value,
                                                          self.enums.Data.Content.value))
        self.contact_page.sign_email_respond()
        self.contact_page.sign_agreement()


if __name__ == "__main__":
    ENV = os.environ.get('env')
    unittest.main()
