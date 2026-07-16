import json


class Graph:
    def __init__(self, name):
        self.name = name

    def toJSON(self):
        return {"name": self.name}

    def fromJSON(self, json):
        return Graph(json["name"])
