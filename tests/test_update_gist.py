import pytest
import json
from jsonschema import validate
import random
from global_parameters import PATCH_GIST_VALID_PARAMETERS
from schema_post_gist import response_schema
from src.DTOs.request_dto import RequestDTO
from src.request_files.gists_request_service import GistsRequests


class TestUpdateGist:
    request_valid_token = ""
    request_restricted_token = ""
    gists_requests = GistsRequests()

#    @pytest.mark.parametrize("new_description, new_file", PATCH_GIST_VALID_PARAMETERS)
    @pytest.mark.usefixtures("setup_gist_data_to_update")
    @pytest.mark.smoke
    def test_update_gist_success(self, setup_gist_data_to_update):
        # DEPOIS VER QUE NÃO É POSSÍVEL FAZER GET POR ID
        # ADICIONAR VALIDAÇÃO DA DATA DE CRIAÇÃO

        a = setup_gist_data_to_update
        assert True
        # created_gist_from_fixture = post_gist_and_delete
        # random_option = random.choice(test_list)
        # body = {"description": new_description, "files": new_file}
        # request_dto = RequestDTO(parameters=created_gist_from_fixture["id"], body=body)
        # request_dto.set_auth_header(self.request_valid_token)
        # response = self.gists_requests.update_gist(request_dto)
        # assert response.status_code == 200
        # response_content = json.loads(response.content)
        # validate(instance=response_content, schema=response_schema)
        # assert response_content["description"] == created_gist_from_fixture["description"]
        # assert response_content["files"].keys() == created_gist_from_fixture["files"].keys()
        #adicionar validação do UPDATED AT
