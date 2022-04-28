import json


class GistsDTO:

    def __init__(self, gist_id, description=None, public=None):
        self._id = gist_id
        self._description = description
        self._public = public

    def get_attributes_as_json(self):
        return json.dumps(self.__dict__)