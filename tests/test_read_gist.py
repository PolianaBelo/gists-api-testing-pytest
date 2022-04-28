import json
import pytest
from jsonschema import validate
from schema_post_gist import response_schema
from src.DTOs.request_dto import RequestDTO
from src.request_files.gists_request_service import GistsRequests


class TestReadGist:
    request_valid_token = ""
    request_restricted_token = ""
    gists_requests = GistsRequests()

    @pytest.mark.usefixtures("post_gist_and_delete")
    @pytest.mark.smoke
    def test_read_gist(self, post_gist_and_delete):
        # DEPOIS VER QUE NÃO É POSSÍVEL FAZER GET POR ID
        # ADICIONAR VALIDAÇÃO DA DATA DE CRIAÇÃO
        create_gist_response = post_gist_and_delete
        request_dto = RequestDTO(parameters=create_gist_response["id"])
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.read_gist(request_dto)
        assert response.status_code == 200
        response_content = json.loads(response.content)
        validate(instance=response_content, schema=response_schema)
        assert response_content["description"] == create_gist_response["description"]
        assert response_content["files"].keys() == create_gist_response["files"].keys()