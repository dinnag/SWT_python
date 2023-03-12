# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Test_2", header="Header_2", footer="Footer_2"))
    app.session.logout()

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New_name"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New_header"))
    app.session.logout()