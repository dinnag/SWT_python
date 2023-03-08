# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test_1", header="Header_1", footer="Footer_1"))
    app.session.logout()
