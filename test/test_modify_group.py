# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Test_2", header="Header_2", footer="Footer_2"))

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New_name"))

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New_header"))