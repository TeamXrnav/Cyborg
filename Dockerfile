FROM ryoishin/cyborg:debian

RUN set -ex \
    && git clone -b master https://github.com/TeamXrnav/Cyborg /root/cyborgbot\bin \
    && chmod 777 /root/cyborgbot/bin

WORKDIR /root/cyborgbot/bin/

CMD ["python3", "-m", "cyborgbot", "cyborgbot/bin"]
