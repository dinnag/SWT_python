# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="wqew", middlename="hgfhg", lastname="kjhk", nickname="lklk", title=";kl;l", company=";lgffgfgf", address="hjgjhjk", homephone="khgkhj", mobilephone="khkhk",
                                       workphone="dtgfhgj", fax="gfjfkjf", email="dudfj", email2="utudfdd", email3="jhjhgk", homepage="fhfgjgf", bday="2", bmonth="June", byear="1990", aday="5",
                                       amonth="May", ayear="2000", address2="jhgjhj", phone2="jhjhkj", notes="kjkj"))

