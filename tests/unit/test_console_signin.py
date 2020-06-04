import json
import os
import uuid
import requests
import requests_mock


import pytest

from console_signin.console_signin import SlackMessage


class LambdaContext:
    """Context class that mimics the AWS Lambda context
    http://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    """
    def __init__(self):
        self.aws_request_id = uuid.uuid4().hex

        self.log_group_name = '/aws/lambda/test'
        self.log_stream_name = '2016-11-15blahblah'

        self.function_name = 'test'
        self.memory_limit_in_mb = '384'
        self.function_version = '1'
        self.invoked_function_arn = 'arn:aws:lambda:us-west-2:blahblah:function:test'

        # FIXME(willkg): Keeping these as None until we need them.
        self.client_context = None
        self.identity = None

EVENT_FILE = os.path.join(
    os.path.dirname(__file__),
    '..',
    '..',
    'events',
    'console_sign_in.json'
)

# @pytest.fixture
# def mock_env_slack_web_url(monkeypatch):
#     monkeypatch.setenv("slackWebhookURL", "https://hooks.slack.com/workflows/foo/bar/")


@pytest.fixture()
def event(event_file=EVENT_FILE):
    '''Trigger event'''
    with open(event_file) as f:
        return json.load(f)

def test_slack_message_happy_path():
    msg = SlackMessage("arn:aws:iam::123456789012:user/doug@1strategy.com")

    with requests_mock.Mocker() as m:
        m.post("https://hooks.slack.com/workflows/valid/path")
        resp = msg.post("https://hooks.slack.com/workflows/valid/path")

    assert resp.status_code == 200

def test_slack_message_invalid_url():
    msg = SlackMessage("arn:aws:iam::123456789012:user/doug@1strategy.com")
    resp_body = {
        "error": "invalid_token",
        "ok": False,
        "response_metadata": {
            "messages": []
        }
    }
    with requests_mock.Mocker() as m:
        m.post("https://hooks.slack.com/workflows/invalid/token", json=resp_body, status_code=401)
        resp = msg.post("https://hooks.slack.com/workflows/invalid/token")

    assert resp.status_code == 401
