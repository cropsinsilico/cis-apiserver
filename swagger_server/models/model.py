# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.com import Com  # noqa: F401,E501
from swagger_server.models.model_driver import ModelDriver  # noqa: F401,E501
from swagger_server import util


class Model(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, description: str=None, driver: ModelDriver=None, args: str=None, client_of: str=None, is_server: str=None, inputs: List[Com]=None, outputs: List[Com]=None):  # noqa: E501
        """Model - a model defined in Swagger

        :param id: The id of this Model.  # noqa: E501
        :type id: int
        :param name: The name of this Model.  # noqa: E501
        :type name: str
        :param description: The description of this Model.  # noqa: E501
        :type description: str
        :param driver: The driver of this Model.  # noqa: E501
        :type driver: ModelDriver
        :param args: The args of this Model.  # noqa: E501
        :type args: str
        :param client_of: The client_of of this Model.  # noqa: E501
        :type client_of: str
        :param is_server: The is_server of this Model.  # noqa: E501
        :type is_server: str
        :param inputs: The inputs of this Model.  # noqa: E501
        :type inputs: List[Com]
        :param outputs: The outputs of this Model.  # noqa: E501
        :type outputs: List[Com]
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'description': str,
            'driver': ModelDriver,
            'args': str,
            'client_of': str,
            'is_server': str,
            'inputs': List[Com],
            'outputs': List[Com]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'driver': 'driver',
            'args': 'args',
            'client_of': 'client_of',
            'is_server': 'is_server',
            'inputs': 'inputs',
            'outputs': 'outputs'
        }

        self._id = id
        self._name = name
        self._description = description
        self._driver = driver
        self._args = args
        self._client_of = client_of
        self._is_server = is_server
        self._inputs = inputs
        self._outputs = outputs

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Model.

        The primary key for this model  # noqa: E501

        :return: The id of this Model.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Model.

        The primary key for this model  # noqa: E501

        :param id: The id of this Model.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Model.

        The short name / identifier of this model  # noqa: E501

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Model.

        The short name / identifier of this model  # noqa: E501

        :param name: The name of this Model.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Model.

        Long name / description of this model  # noqa: E501

        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Model.

        Long name / description of this model  # noqa: E501

        :param description: The description of this Model.
        :type description: str
        """

        self._description = description

    @property
    def driver(self) -> ModelDriver:
        """Gets the driver of this Model.


        :return: The driver of this Model.
        :rtype: ModelDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver: ModelDriver):
        """Sets the driver of this Model.


        :param driver: The driver of this Model.
        :type driver: ModelDriver
        """
        if driver is None:
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def args(self) -> str:
        """Gets the args of this Model.

        Path to the model source code on disk  # noqa: E501

        :return: The args of this Model.
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args: str):
        """Sets the args of this Model.

        Path to the model source code on disk  # noqa: E501

        :param args: The args of this Model.
        :type args: str
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def client_of(self) -> str:
        """Gets the client_of of this Model.

        Denotes that the model is the client in some context  # noqa: E501

        :return: The client_of of this Model.
        :rtype: str
        """
        return self._client_of

    @client_of.setter
    def client_of(self, client_of: str):
        """Sets the client_of of this Model.

        Denotes that the model is the client in some context  # noqa: E501

        :param client_of: The client_of of this Model.
        :type client_of: str
        """

        self._client_of = client_of

    @property
    def is_server(self) -> str:
        """Gets the is_server of this Model.

        Denotes that the model is the server in some context  # noqa: E501

        :return: The is_server of this Model.
        :rtype: str
        """
        return self._is_server

    @is_server.setter
    def is_server(self, is_server: str):
        """Sets the is_server of this Model.

        Denotes that the model is the server in some context  # noqa: E501

        :param is_server: The is_server of this Model.
        :type is_server: str
        """

        self._is_server = is_server

    @property
    def inputs(self) -> List[Com]:
        """Gets the inputs of this Model.

        Input Coms associated with this Model  # noqa: E501

        :return: The inputs of this Model.
        :rtype: List[Com]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs: List[Com]):
        """Sets the inputs of this Model.

        Input Coms associated with this Model  # noqa: E501

        :param inputs: The inputs of this Model.
        :type inputs: List[Com]
        """
        if inputs is None:
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

    @property
    def outputs(self) -> List[Com]:
        """Gets the outputs of this Model.

        Output Coms associated with this Model  # noqa: E501

        :return: The outputs of this Model.
        :rtype: List[Com]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs: List[Com]):
        """Sets the outputs of this Model.

        Output Coms associated with this Model  # noqa: E501

        :param outputs: The outputs of this Model.
        :type outputs: List[Com]
        """
        if outputs is None:
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs
