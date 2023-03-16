import json

class ProjectEdit():
    def __init__(self, project_location):
        self.project_location = project_location
        self.properties = ['source', 'start', 'end', 'is_reverse', 'speed']