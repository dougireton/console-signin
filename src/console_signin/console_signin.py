import os
import re

import beeline
import requests
from aws_lambda_powertools.logging import Logger
from beeline.middleware.awslambda import beeline_wrapper

beeline.init(
    # Get this via https://ui.honeycomb.io/account after signing up for Honeycomb
    writekey='d2c268adc6ba3802eb7ba81dcd2e545e',
    # The name of your app is a good choice to start with
    dataset='console-signin',
    service_name='console-signin',
    # debug=True, # defaults to False. if True, data doesn't get sent to Honeycomb
)

logger = Logger(service="Console Sign-in")

class SlackMessage:
    def __init__(self, user_arn):
        self.user_arn = user_arn

    def _user_name(self):
        """
        Extracts the username from an AWS User ARN

        Parameters:
            self.user_arn (string): AWS User ARN, e.g. arn:aws:iam::123456789012:user/doug@example.com

        Returns:
            username (string): Username in email format, e.g. doug@example.com
        """
        arn = re.search(r'arn:aws:iam::\d{12}:user/([a-z]+@\w+\.com)', self.user_arn)
        return arn.group(1)

    def _payload(self) -> dict:
        p = {'username': self._user_name()}
        return p
        
    def post(self, slack_url: str) -> requests.Response:
        logger.debug(f"POSTing {self._payload()} to {slack_url}")

        resp = requests.post(slack_url, json=self._payload())
        logger.debug(f"POST to {slack_url} returned: {resp}")
        return resp

@beeline_wrapper
def lambda_handler(event, context):
    """Sample Lambda function reacting to EventBridge events

    Parameters
    ----------
    event: dict, required
        Event Bridge Events Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
        Response status code from Slack API call
    """
    master_acct_arn = event["detail"]["additionalEventData"]["SwitchFrom"]
    beeline.add_context({"user_arn": master_acct_arn})
    sm = SlackMessage(master_acct_arn)
    resp = sm.post(os.environ["slackWebhookURL"])

    if resp.status_code != requests.codes.ok:
        resp.raise_for_status()

    logger.info(f"Posting to Slack channel returned {resp}.")
    return resp.status_code
