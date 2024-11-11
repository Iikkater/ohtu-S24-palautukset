from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        name = data.get("tool", {}).get("poetry", {}).get("name")
        description = data.get("tool", {}).get("poetry", {}).get("description")
        license = data.get("tool", {}).get("poetry", {}).get("license")
        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
