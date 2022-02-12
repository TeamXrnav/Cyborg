FROM ryoishin/cyborg:debian

RUN set -ex \
    && git clone -b master https://github.com/TeamXrnav/Cyborg /root/cyborgbot \
    && chmod 777 /root/cyborgbot

WORKDIR /root/cyborgbot/

CMD ["python3", "-m", "cyborgbot"]
