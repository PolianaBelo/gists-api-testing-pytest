import json

import pytest
from global_parameters import POST_GIST_VALID_PARAMETERS, PATCH_GIST_VALID_PARAMETERS
from src.DTOs.request_dto import RequestDTO
from src.request_files.gists_request_service import GistsRequests


@pytest.fixture(params=POST_GIST_VALID_PARAMETERS)
def post_gist(request):
    gists_requests = GistsRequests()
    request_valid_token = "token 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"
    valid_description, valid_file, is_public = request.param
    body = {"description": valid_description, "files": valid_file, "public": is_public}
    request_dto = RequestDTO(body)
    request_dto.set_auth_header(request_valid_token)
    response = gists_requests.post_gists(request_dto)
    yield json.loads(response.content)


@pytest.fixture
def post_gist_and_delete(post_gist):
    gists_requests = GistsRequests()
    request_valid_token = "token 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"
    response_from_post = post_gist
    yield response_from_post
    request_dto = RequestDTO(parameters=response_from_post["id"])
    request_dto.set_auth_header(request_valid_token)
    gists_requests.delete_gist(request_dto)


@pytest.fixture(params=PATCH_GIST_VALID_PARAMETERS)
def setup_update_parameters(request):
    new_description, new_file = request.param
    body = {"description": new_description, "files": new_file}
    yield body


@pytest.fixture
def setup_gist_data_to_update(setup_update_parameters, post_gist_and_delete):
    gists_requests = GistsRequests()
    request_valid_token = "token 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"
    response_from_post = post_gist_and_delete
    yield [setup_update_parameters, response_from_post]
    request_dto = RequestDTO(parameters=response_from_post["id"])
    request_dto.set_auth_header(request_valid_token)
    gists_requests.delete_gist(request_dto)