__author__ = 'Arseniy'
from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.get_project_list()) == 0:
        app.project.create(Project("test project"))

    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.soap.get_project_list()
    assert project not in new_projects

