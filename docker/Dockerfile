FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 ffmpeg jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir mediainfo-generator && \
    mkdir /config
    # pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ mediainfo-generator && \

WORKDIR /config

VOLUME [ "/config" ]

ENTRYPOINT [ "mediainfo-generator" ]