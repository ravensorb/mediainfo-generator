#!/usr/bin/env python3

#######################################################################

import logging
import os
import readchar
import signal

from mediainfo_generator.utils.settings_utils_v1 import globalSettingsMgr
from mediainfo_generator.utils.logging_utils import setup_logging
from mediainfo_generator.utils.cli_args import globalArgs
from mediainfo_generator.utils.media_utils import MediaInfoScanner

#######################################################################

#######################################################################

def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == "y":
        print("")
        os._exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)  # clear the printed line
        print("    ", end="\r", flush=True)

signal.signal(signal.SIGINT, handler)

#######################################################################

setup_logging(
    str(globalSettingsMgr.modulePath.joinpath("logging.yaml")),
)

logger = logging.getLogger("mediainfo_generator")
logger.setLevel(getattr(logging, globalArgs.logLevel))

globalSettingsMgr.loadFromFile("config.yaml", globalArgs)

#######################################################################

def cli():
    scanner = MediaInfoScanner() 
    scanner.execute()

#######################################################################
#######################################################################

if __name__ == "__main__":
    cli()
