__author__ = 'Arseniy'
from model.project import Project
import string
import random


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.login("administrator", "root")
    project = Project(name=random_name("proj_", 10))
    if project in app.soap.get_project_list():
        app.project.delete(project)

    old_projects = app.soap.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
