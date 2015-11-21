__author__ = 'Arseniy'
from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        soap_list = client.service.mc_projects_get_user_accessible(self.app.config["webadmin"]["username"],
                                                                   self.app.config["webadmin"]["password"])
        proj_list = [Project(name=e.name, description=e.description) for e in soap_list]
        return proj_list
