# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="wqew", middlename="hgfhg", lastname="kjhk", nickname="lklk", title=";kl;l", company=";lgffgfgf", address="hjgjhjk", home="khgkhj", mobile="khkhk",
                        work="dtgfhgj", fax="gfjfkjf", email="dudfj", email2="utudfdd", email3="jhjhgk", homepage="fhfgjgf", bday="2", bmonth="June", byear="1990", aday="5",
                        amonth="May", ayear="2000", address2="jhgjhj", phone2="jhjhkj", notes="kjkj"))
    app.logout()
