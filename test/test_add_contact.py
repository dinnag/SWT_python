# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="wqew", middlename="hgfhg", lastname="kjhk", nickname="lklk", title=";kl;l", company=";lgffgfgf", address="hjgjhjk", homephone="khgkhj", mobilephone="khkhk",
                                       workphone="dtgfhgj", fax="gfjfkjf", email="dudfj", email2="utudfdd", email3="jhjhgk", homepage="fhfgjgf", bday="2", bmonth="June", byear="1990", aday="5",
                                       amonth="May", ayear="2000", address2="jhgjhj", phone2="jhjhkj", notes="kjkj"))
    app.session.logout()

