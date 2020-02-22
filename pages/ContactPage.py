from selenium.webdriver.common.keys import Keys
from seleniumpagefactory.Pagefactory import PageFactory


class ContactPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "business_client_type": ('XPATH', '//label[contains(.,"klient biznesowy")]'),
        "name": ('ID', 'name'),
        "email": ('ID', 'email_c'),
        "company_name": ('ID', 'company_name'),
        "phone": ('ID', 'phone'),
        "subject_container": ('ID', 'select2-subject-container'),
        "subject_input": ("XPATH", '//input[@type="search"]'),
        "text_area": ('ID', 'body'),
        "respond_type": ('XPATH', '//label[contains(.,"e-mail") and @class="form__radio"]'),
        "agreement_text": ('XPATH', '//div[@class="js__expand-pre" and contains(text(),"Wyrażam")]')
    }

    def chose_client_type(self):
        self.business_client_type.click_button()

    def type_name(self, type_name):
        self.name.set_text(type_name)

    def type_email(self, email):
        self.email.set_text(email)

    def type_company_name(self, company_name):
        self.company_name.set_text(company_name)

    def type_phone(self, phone_number):
        self.phone.set_text(phone_number)

    def chose_subject(self, subject):
        self.subject_container.click_button()
        self.subject_input.set_text(subject)
        self.subject_input.set_text(Keys.ENTER)

    def type_content(self, content):
        self.text_area.set_text(content)

    def sign_email_respond(self):
        self.respond_type.click_button()

    def sign_agreement(self):
        self.agreement_text.hover()
        self.agreement_text.click_button()
