#!/usr/bin/env python3

#######################################################################

from typing import List
from enum import Enum

import logging
import os
import json
from pathlib import Path

import confuse
import importlib_resources
# import jsonpickle
# from dotenv import load_dotenv
# from expandvars import expandvars

#######################################################################

class SettingsPath:
    data: str
    output: str

    def __init__(self, data: str, output: str) -> None:
        self.data = data
        self.output = output

        if self.output is None:
            self.output = self.data

class Settings:
    version: str
    path: SettingsPath

    def __init__(self, version: str, path: SettingsPath) -> None:
        self.version = version
        self.path = path

#######################################################################

class SettingsManager:
    _config: confuse.Configuration
    settings: Settings
    modulePath: Path

    def __init__(self) -> None:
        self._logger = logging.getLogger("mediainfo_generator")
        self.modulePath = Path(str(importlib_resources.files("mediainfo_generator")))

    def loadFromFile(self, fileName: str, cmdLineArgs=None) -> None:
        self._logger.debug("Loading Configuration")

        self._config = confuse.Configuration("mediainfo_generator", "mediainfo_generator")

        self._logger.debug("Loading Configuration from Default Configuration")
        self._config._add_default_source()
        self._config._add_user_source()

        if os.path.exists(self.modulePath.joinpath("config_default.yaml")):
            self._config.set_file(self.modulePath.joinpath("config_default.yaml"))

        if os.path.exists(fileName):
            self._logger.debug("Loading Configuration from User Configuration: '{}'".format(fileName))
            self._config.set_file(fileName)

        # self._logger.debug("Loading Configuration from Environment")
        # load_dotenv(Path(os.getcwd(), ".env"))
        # self._config.set_env("PMMCFG")

        if cmdLineArgs is not None:
            self._logger.debug("Loading Configuration from Command Line")
            self._logger.debug("Command Line Args: {}".format(cmdLineArgs))
            self._config.set_args(cmdLineArgs, dots=True)

        self._logger.debug(
            "Configuration Directory: {}".format(self._config.config_dir())
        )
        self._logger.debug(
            "User Configuration Path: {}".format(self._config.user_config_path())
        )

        self._logger.debug("Loaded Configuration:")

        self.settings = Settings(
            version=self._config["version"].get(confuse.Optional(str)),  # type: ignore
            path=SettingsPath(
                data=self._config["path"]["data"].get(confuse.Optional(str)),  # type: ignore
                output=self._config["path"]["output"].get(confuse.Optional(str)),  # type: ignore
            )
        )

        #self._logger.debug("Active Settings:")
        #self._logger.debug("{}".format(json.dumps(self.settings, indent=4)))

#######################################################################

globalSettingsMgr = SettingsManager()
