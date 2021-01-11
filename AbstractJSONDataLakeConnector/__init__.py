# -*- coding: utf-8 -*-
""" Abstract JSONDataLakeConnection interface

This module specifies the interface of a generic json-only data lake connector.
"""

from abc import ABC, abstractmethod


class JSONDataLakeConnection(ABC):

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def pwd(self) -> str:
        """ Returns the current remote data lake path """
        pass

    @abstractmethod
    def cd(self, path: str):
        """ Change current path. Will raise error if the specified path does not exist """
        pass

    @abstractmethod
    def mkdir(self, path: str):
        """ Create new empty directory inside current working directory. Absolute path not supported. """
        pass

    @abstractmethod
    def rmdir(self, path: str):
        """ Delete specified directory and all its content. Target directory has to be inside the current working directory. Absolute path not supported."""
        pass

    @abstractmethod
    def store(self, serialized_json_content: str, filename: str, overwrite: bool):
        """ Store a file inside the current working directory """
        pass

    @abstractmethod
    def retrieve(self, filename: str) -> dict:
        """ Retrieve a file from the current working directory """
        pass

    @abstractmethod
    def rm(self, filename: str):
        """ Remove specified file from the current working directory """
        pass

    @abstractmethod
    def ls(self) -> [str]:
        """ Returns a list of the content of the current working directory """
        pass
