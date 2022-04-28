from src.request_files.gists_request_service import GistsRequests


class GistsRequestController:
    gists_request = GistsRequests()

    def create_gist(self, gist_dto):

        response = self.gists_request.post_gists()