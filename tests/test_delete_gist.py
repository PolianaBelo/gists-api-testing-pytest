import json

import pytest

from src.DTOs.request_dto import RequestDTO
from src.request_files.gists_request_service import GistsRequests


class TestDeleteGist:
    request_valid_token = ""
    request_restricted_token = ""
    gists_requests = GistsRequests()

    @pytest.mark.usefixtures("post_gist")
    @pytest.mark.smoke
    def test_delete_gist(self, post_gist):
        # DEPOIS VER QUE NÃO É POSSÍVEL FAZER GET POR ID
        # ADICIONAR VALIDAÇÃO DA DATA DE CRIAÇÃO
        create_gist_response = post_gist
        request_dto = RequestDTO(parameters=create_gist_response["id"])
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.delete_gist(request_dto)
        assert response.status_code == 204
        assert response.text == ""

    #@pytest.mark.usefixtures("post_gist")
    @pytest.mark.smoke
    def test_delete_gist_resource_not_found(self):
        # USAR MAIS INPUTS
        non_existent_gist_id = "00001234"
        request_dto = RequestDTO(parameters=non_existent_gist_id)
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.delete_gist(request_dto)
        assert response.status_code == 404
        assert response.text == '{"message":"Not Found","documentation_url":"https://docs.github.com/rest/reference/gists#delete-a-gist"}'

    @pytest.mark.usefixtures("post_gist_and_delete")
    @pytest.mark.smoke
    def test_delete_gist_unauthorized(self, post_gist_and_delete):
        # USAR MAIS INPUTS
        # TESTAR NO FINAL SE REGISTRO AINDA PODE SER RECUPERADO PELO GET
        # Adicionar deleção
        create_gist_response = post_gist_and_delete
        request_dto = RequestDTO(parameters=create_gist_response["id"])
        request_dto.set_auth_header(self.request_restricted_token)
        response = self.gists_requests.delete_gist(request_dto)
        assert response.status_code == 401
        assert response.text == '{"message":"Bad credentials","documentation_url":"https://docs.github.com/rest"}'

    @pytest.mark.usefixtures("post_gist_and_delete")
    @pytest.mark.smoke
    def test_delete_gist_unauthorized2(self, post_gist_and_delete):
        # VER COMO DELETAR HEADER DE USER-AGENT
        assert True