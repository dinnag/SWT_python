# -*- coding: utf-8 -*-
from model.group import Group

def test_modif_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group(Group(name="Test_2", header="Header_2", footer="Footer_2"))
    app.session.logout()