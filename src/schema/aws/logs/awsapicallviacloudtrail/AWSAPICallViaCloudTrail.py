# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.logs.awsapicallviacloudtrail.RequestParameters import RequestParameters  # noqa: F401,E501
from schema.aws.logs.awsapicallviacloudtrail.UserIdentity import UserIdentity  # noqa: F401,E501

class AWSAPICallViaCloudTrail(object):


    _types = {
        'requestParameters': 'RequestParameters',
        'userIdentity': 'UserIdentity',
        'eventID': 'str',
        'awsRegion': 'str',
        'eventVersion': 'str',
        'responseElements': 'object',
        'sourceIPAddress': 'str',
        'eventSource': 'str',
        'errorMessage': 'str',
        'errorCode': 'str',
        'userAgent': 'str',
        'eventType': 'str',
        'apiVersion': 'str',
        'requestID': 'str',
        'eventTime': 'datetime',
        'eventName': 'str'
    }

    _attribute_map = {
        'requestParameters': 'requestParameters',
        'userIdentity': 'userIdentity',
        'eventID': 'eventID',
        'awsRegion': 'awsRegion',
        'eventVersion': 'eventVersion',
        'responseElements': 'responseElements',
        'sourceIPAddress': 'sourceIPAddress',
        'eventSource': 'eventSource',
        'errorMessage': 'errorMessage',
        'errorCode': 'errorCode',
        'userAgent': 'userAgent',
        'eventType': 'eventType',
        'apiVersion': 'apiVersion',
        'requestID': 'requestID',
        'eventTime': 'eventTime',
        'eventName': 'eventName'
    }

    def __init__(self, requestParameters=None, userIdentity=None, eventID=None, awsRegion=None, eventVersion=None, responseElements=None, sourceIPAddress=None, eventSource=None, errorMessage=None, errorCode=None, userAgent=None, eventType=None, apiVersion=None, requestID=None, eventTime=None, eventName=None):  # noqa: E501
        self._requestParameters = None
        self._userIdentity = None
        self._eventID = None
        self._awsRegion = None
        self._eventVersion = None
        self._responseElements = None
        self._sourceIPAddress = None
        self._eventSource = None
        self._errorMessage = None
        self._errorCode = None
        self._userAgent = None
        self._eventType = None
        self._apiVersion = None
        self._requestID = None
        self._eventTime = None
        self._eventName = None
        self.discriminator = None
        self.requestParameters = requestParameters
        self.userIdentity = userIdentity
        self.eventID = eventID
        self.awsRegion = awsRegion
        self.eventVersion = eventVersion
        self.responseElements = responseElements
        self.sourceIPAddress = sourceIPAddress
        self.eventSource = eventSource
        self.errorMessage = errorMessage
        self.errorCode = errorCode
        self.userAgent = userAgent
        self.eventType = eventType
        self.apiVersion = apiVersion
        self.requestID = requestID
        self.eventTime = eventTime
        self.eventName = eventName


    @property
    def requestParameters(self):

        return self._requestParameters

    @requestParameters.setter
    def requestParameters(self, requestParameters):


        self._requestParameters = requestParameters


    @property
    def userIdentity(self):

        return self._userIdentity

    @userIdentity.setter
    def userIdentity(self, userIdentity):


        self._userIdentity = userIdentity


    @property
    def eventID(self):

        return self._eventID

    @eventID.setter
    def eventID(self, eventID):


        self._eventID = eventID


    @property
    def awsRegion(self):

        return self._awsRegion

    @awsRegion.setter
    def awsRegion(self, awsRegion):


        self._awsRegion = awsRegion


    @property
    def eventVersion(self):

        return self._eventVersion

    @eventVersion.setter
    def eventVersion(self, eventVersion):


        self._eventVersion = eventVersion


    @property
    def responseElements(self):

        return self._responseElements

    @responseElements.setter
    def responseElements(self, responseElements):


        self._responseElements = responseElements


    @property
    def sourceIPAddress(self):

        return self._sourceIPAddress

    @sourceIPAddress.setter
    def sourceIPAddress(self, sourceIPAddress):


        self._sourceIPAddress = sourceIPAddress


    @property
    def eventSource(self):

        return self._eventSource

    @eventSource.setter
    def eventSource(self, eventSource):


        self._eventSource = eventSource


    @property
    def errorMessage(self):

        return self._errorMessage

    @errorMessage.setter
    def errorMessage(self, errorMessage):


        self._errorMessage = errorMessage


    @property
    def errorCode(self):

        return self._errorCode

    @errorCode.setter
    def errorCode(self, errorCode):


        self._errorCode = errorCode


    @property
    def userAgent(self):

        return self._userAgent

    @userAgent.setter
    def userAgent(self, userAgent):


        self._userAgent = userAgent


    @property
    def eventType(self):

        return self._eventType

    @eventType.setter
    def eventType(self, eventType):


        self._eventType = eventType


    @property
    def apiVersion(self):

        return self._apiVersion

    @apiVersion.setter
    def apiVersion(self, apiVersion):


        self._apiVersion = apiVersion


    @property
    def requestID(self):

        return self._requestID

    @requestID.setter
    def requestID(self, requestID):


        self._requestID = requestID


    @property
    def eventTime(self):

        return self._eventTime

    @eventTime.setter
    def eventTime(self, eventTime):


        self._eventTime = eventTime


    @property
    def eventName(self):

        return self._eventName

    @eventName.setter
    def eventName(self, eventName):


        self._eventName = eventName

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AWSAPICallViaCloudTrail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AWSAPICallViaCloudTrail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

