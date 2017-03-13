# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems


class Params5(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, repo_url=None):
        """Params5 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'repo_url': 'str'
        }

        self.attribute_map = {
            'repo_url': 'repo_url'
        }

        self._repo_url = repo_url

    @property
    def repo_url(self):
        """Gets the repo_url of this Params5.

        Base repository URL for remotely generated repo

        :return: The repo_url of this Params5.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this Params5.

        Base repository URL for remotely generated repo

        :param repo_url: The repo_url of this Params5.
        :type: str
        """

        self._repo_url = repo_url

    def to_dict(self):
        """Returns the model properties as a dict """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model """
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint` """
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal """
        if not isinstance(other, Params5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other
