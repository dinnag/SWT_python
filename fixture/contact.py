from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_homepage()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("email", contact.email)
        self.change_list_value("bday", contact.bday)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_list_value("aday", contact.aday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_list_value(self, field_name, contact):
        wd = self.app.wd
        if contact is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(contact)

    def change_field_value(self, field_name, contact):
        wd = self.app.wd
        if contact is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(contact)
    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.app.navigation.return_to_homepage()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        # submit group modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.return_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                firstname = element.find_element_by_xpath("./td[3]").text
                lastname = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
