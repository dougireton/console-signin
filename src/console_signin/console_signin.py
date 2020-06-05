import os
import re

import requests

from aws_lambda_powertools.logging import Logger

# "https://hooks.slack.com/workflows/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"

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
        The same input event file
    """
    master_acct_arn = event["detail"]["additionalEventData"]["SwitchFrom"]
    sm = SlackMessage(master_acct_arn)
    resp = sm.post(os.environ["slackWebhookURL"])

    if resp.status_code != requests.codes.ok:
        resp.raise_for_status()

    logger.info(f"Posting to Slack channel returned {resp}.")
    return resp.status_code