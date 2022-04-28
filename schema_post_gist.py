response_schema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": "http://example.com/example.json",
        "type": "object",
        "title": "The root schema",
        "description": "The root schema comprises the entire JSON document.",
        "default": {},
        "examples": [
            {
                "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
                "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
                "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
                "id": "aa5a315d61ae9438b18d",
                "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
                "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
                "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
                "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
                "created_at": "2010-04-14T02:15:15Z",
                "updated_at": "2011-06-20T11:34:15Z",
                "description": "Hello World Examples",
                "comments": 0,
                "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/"
            }
        ],
        "required": [
            "url",
            "forks_url",
            "commits_url",
            "id",
            "node_id",
            "git_pull_url",
            "git_push_url",
            "html_url",
            "created_at",
            "updated_at",
            "comments",
            "comments_url"
        ],
        "properties": {
            "url": {
                "$id": "#/properties/url",
                "type": "string",
                "title": "The url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://api.github.com/gists/aa5a315d61ae9438b18d"
                ]
            },
            "forks_url": {
                "$id": "#/properties/forks_url",
                "type": "string",
                "title": "The forks_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://api.github.com/gists/aa5a315d61ae9438b18d/forks"
                ]
            },
            "commits_url": {
                "$id": "#/properties/commits_url",
                "type": "string",
                "title": "The commits_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://api.github.com/gists/aa5a315d61ae9438b18d/commits"
                ]
            },
            "id": {
                "$id": "#/properties/id",
                "type": "string",
                "title": "The id schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "aa5a315d61ae9438b18d"
                ]
            },
            "node_id": {
                "$id": "#/properties/node_id",
                "type": "string",
                "title": "The node_id schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk"
                ]
            },
            "git_pull_url": {
                "$id": "#/properties/git_pull_url",
                "type": "string",
                "title": "The git_pull_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://gist.github.com/aa5a315d61ae9438b18d.git"
                ]
            },
            "git_push_url": {
                "$id": "#/properties/git_push_url",
                "type": "string",
                "title": "The git_push_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://gist.github.com/aa5a315d61ae9438b18d.git"
                ]
            },
            "html_url": {
                "$id": "#/properties/html_url",
                "type": "string",
                "title": "The html_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://gist.github.com/aa5a315d61ae9438b18d"
                ]
            },
            "created_at": {
                "$id": "#/properties/created_at",
                "type": "string",
                "title": "The created_at schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "2010-04-14T02:15:15Z"
                ]
            },
            "updated_at": {
                "$id": "#/properties/updated_at",
                "type": "string",
                "title": "The updated_at schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "2011-06-20T11:34:15Z"
                ]
            },
            "description": {
                "$id": "#/properties/description",

                "title": "The description schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "Hello World Examples"
                ]
            },
            "comments": {
                "$id": "#/properties/comments",
                "type": "integer",
                "title": "The comments schema",
                "description": "An explanation about the purpose of this instance.",
                "default": 0,
                "examples": [
                    0
                ]
            },
            "comments_url": {
                "$id": "#/properties/comments_url",
                "type": "string",
                "title": "The comments_url schema",
                "description": "An explanation about the purpose of this instance.",
                "default": "",
                "examples": [
                    "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/"
                ]
            }
        },
        "additionalProperties": True
    }