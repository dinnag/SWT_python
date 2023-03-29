# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Test_1", header="Header_1", footer="Footer_1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)