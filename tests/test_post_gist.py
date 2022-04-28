import pytest
import json
from requests import Request, Session
from schema_post_gist import response_schema
from global_parameters import POST_GIST_VALID_PARAMETERS
from jsonschema import validate
from src.DTOs.request_dto import RequestDTO
from src.DTOs.gists_dto import GistsDTO
from src.request_files.gists_request_service import GistsRequests


@pytest.mark.smoke
class TestPostGist:
    request_valid_token = "token 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"
    request_restricted_token = "token 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"
    gists_requests = GistsRequests()

    @pytest.mark.parametrize("valid_description, valid_file, is_public", POST_GIST_VALID_PARAMETERS)
    @pytest.mark.smoke
    def test_post_gists_sending_all_fields(self, valid_description, valid_file, is_public):
        # DEPOIS VER QUE É POSSÍVEL FAZER GET
        # lembrar de ter input com vários arquivos e com diferentes formatos e conteúdo repetido
        # ADICIONAR VALIDAÇÃO DA DATA DE CRIAÇÃO
        #NO FINAL VER QUE VALOR É DIFERENTE DO ANTERIOR EM DESCRICAO E FILE
        body = {"description": valid_description, "files": valid_file, "public": is_public}
        request_dto = RequestDTO(body=body)
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.post_gists(request_dto)
        response_content = json.loads(response.content)
        request_dto._parameters = response_content["id"]
        assert response.status_code == 201
        response_content = json.loads(response.content)
        validate(instance=response_content, schema=response_schema)
        assert response_content["description"] == body["description"]
        assert response_content["files"].keys() == body["files"].keys()
        self.tear_down(request_dto)

    def test_post_gists_sending_mandatory_fields(self):
        body = {"files": {"tititi.pdf": {"content": "contentssssssss"}}}
        request_dto = RequestDTO(body)
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.post_gists(request_dto)
        assert response.status_code == 201
        response_content = json.loads(response.content)
        validate(instance=response_content, schema=response_schema)
        assert response_content["files"].keys() == body["files"].keys()

    def test_post_gists_not_modified(self):
        # nao sei se consigo reproduzir
        assert True

    def test_post_gists_forbidden(self):
        # https://stackoverflow.com/questions/70923969/how-to-remove-the-user-agent-header-when-send-request-in-python
        assert True

    def test_post_gists_resource_not_found(self):
        # no input tentar enviar diferentes bodys
        body = {"files": {"tititi.pdf": {"content": "contentssssssss"}}}
        request_dto = RequestDTO(body)
        request_dto.set_auth_header(self.request_restricted_token)
        response = self.gists_requests.post_gists(request_dto)
        assert response.status_code == 404
        assert response.text == '{"message":"Requires authentication","documentation_url":"https://docs.github.com/rest/reference/gists#create-a-gist"}'

    def test_post_gists_validation_failed(self):
        body = {"Batata": {"tititi.pdf": {"content": "contentssssssss"}}}
        request_dto = RequestDTO(body)
        request_dto.set_auth_header(self.request_valid_token)
        response = self.gists_requests.post_gists(request_dto)
        assert response.status_code == 422
        assert response.text == '{"message":"Invalid request.\\n\\n\\"files\\" wasn\'t supplied.","documentation_url":"https://docs.github.com/rest/reference/gists#create-a-gist"}'

    def test_post_gists_unauthorized(self):
        # tentar enviar sem token ou con token inválido
        body = {"files": {"tititi.pdf": {"content": "contentssssssss"}}}
        request_dto = RequestDTO(body)
        request_dto.set_auth_header("")
        response = self.gists_requests.post_gists(request_dto)
        assert response.status_code == 401
        assert response.text == '{"message":"Requires authentication","documentation_url":"https://docs.github.com/rest/reference/gists#create-a-gist"}'

    def tear_down(self, request_dto):
        self.gists_requests.delete_gist(request_dto)
