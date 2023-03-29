# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Test_2", header="Header_2", footer="Footer_2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)