#!/usr/bin/env python3
###################################################################################################

import argparse

###################################################################################################

globalArgParser = argparse.ArgumentParser()

globalArgParser.add_argument(
    "--path.data", 
    help="Root path to scan"
)
globalArgParser.add_argument(
    "--path.output", 
    help="Path to store output in"
)

# Advanced Arguments
globalArgParser.add_argument(
    "--logLevel",
    choices=["INFO", "WARN", "DEBUG", "CRITICAL"],
    default="INFO",
    help="Logging Level (default: %(default)s)",
)

###################################################################################################

globalArgs = globalArgParser.parse_args()
