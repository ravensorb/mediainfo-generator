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
globalArgParser.add_argument(
    "--output.individualFiles",
    choices=["ENABLED", "DISABLED", "enabled", "disabled", "yes", "no", "y", "n"],
    default="DISABLED",
    help="Output individual files (default: %(default)s)"
)
globalArgParser.add_argument(
    "--output.combinedFile",
    choices=["ENABLED", "DISABLED", "enabled", "disabled", "yes", "no", "y", "n"],
    default="ENABLED",
    help="Output combined file (default: %(default)s)"
)
globalArgParser.add_argument(
    "--output.summaryFile",
    choices=["ENABLED", "DISABLED", "enabled", "disabled", "yes", "no", "y", "n"],
    default="ENABLED",
    help="Output summary file (default: %(default)s)"
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
