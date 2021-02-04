# -*- coding: utf-8 -*-
""" Abstract Data Lake class

This module specifies the interface of a generic data lake connection.
"""
import json
from abc import ABC, abstractmethod


class AbstractDataLake(ABC):

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
    def store(self, serialized_content: str, path_filename: str, overwrite: bool):
        """ Upload a file """
        pass

    @abstractmethod
    def retrieve(self, path_filename: str) -> [bytes]:
        """ Retrieve a file """
        pass

    def retrieve_json(self, path_filename: str) -> dict:
        return json.loads(self.retrieve(path_filename))

    @abstractmethod
    def rm(self, path_filename: str):
        """ Delete file """
        pass

    @abstractmethod
    def ls(self, path: str) -> [str]:
        """ Returns a list of the content of the specified directory """
        pass

    @abstractmethod
    def mvdir(self, src_path: str, dest_path: str):
        pass

    @abstractmethod
    def mvfile(self, src_path: str, dest_path: str):
        pass
