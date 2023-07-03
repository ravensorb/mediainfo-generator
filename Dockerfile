# Dockerfile
FROM alpine:latest

COPY src/ /

RUN apk --no-cache add ffmpeg jq bash && \
    chmod +x /*.sh 


VOLUME [ "/data" ]

ENTRYPOINT [ "bash", "/process.sh"]
