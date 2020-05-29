# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class RequestParameters(object):


    _types = {
        'logGroupName': 'str',
        'logStreamName': 'str'
    }

    _attribute_map = {
        'logGroupName': 'logGroupName',
        'logStreamName': 'logStreamName'
    }

    def __init__(self, logGroupName=None, logStreamName=None):  # noqa: E501
        self._logGroupName = None
        self._logStreamName = None
        self.discriminator = None
        self.logGroupName = logGroupName
        self.logStreamName = logStreamName


    @property
    def logGroupName(self):

        return self._logGroupName

    @logGroupName.setter
    def logGroupName(self, logGroupName):


        self._logGroupName = logGroupName


    @property
    def logStreamName(self):

        return self._logStreamName

    @logStreamName.setter
    def logStreamName(self, logStreamName):


        self._logStreamName = logStreamName

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
        if issubclass(RequestParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RequestParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

