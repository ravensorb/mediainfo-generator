#!/bin/sh

set -e

. /venv/bin/activate

mediainfo-generate "$@"

