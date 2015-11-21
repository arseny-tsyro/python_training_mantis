__author__ = 'Arseniy'
from suds.client import Client
from model.project import Project


client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
project_list = []

soap_list = client.service.mc_projects_get_user_accessible("administrator", "root")
proj_list = [Project(name=e.name, description=e.description) for e in soap_list]

print(len(proj_list))
for p in proj_list:
    print(p)