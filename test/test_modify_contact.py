# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="test1", middlename="test2", lastname="kjhk", nickname="lklk", title=";kl;l", company=";lgffgfgf", address="hjgjhjk", homephone="khgkhj", mobilephone="khkhk",
                                             workphone="dtgfhgj", fax="gfjfkjf", email="dudfj", email2="utudfdd", email3="jhjhgk", homepage="fhfgjgf", bday="2", bmonth="June", byear="1990", aday="5",
                                             amonth="May", ayear="2000", address2="jhgjhj", phone2="jhjhkj", notes="kjkj"))
    app.session.logout()

def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New_FirstName"))
    app.session.logout()