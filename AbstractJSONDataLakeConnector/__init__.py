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
    def mkdir(self, path: str):
        """ Create new empty directory """
        pass

    @abstractmethod
    def rmdir(self, path: str, recursive: bool = True):
        """ Delete specified directory and all its content. RECURSIVE BY DEFAULT: set recursive=False to raise an error in case the directory has content """
        pass

    @abstractmethod
    def store(self, serialized_json_content: str, path_filename: str, overwrite: bool):
        """ Upload a file """
        pass

    @abstractmethod
    def retrieve(self, path_filename: str) -> dict:
        """ Retrieve a file """
        pass

    @abstractmethod
    def rm(self, path_filename: str):
        """ Delete file """
        pass

    @abstractmethod
    def ls(self, path:str) -> [str]:
        """ Returns a list of the content of the specified directory """
        pass
