FROM ryoishin/cyborg:debian

RUN git clone https://github.com/TeamXrnav/Cyborg.git /root/cyborgbot

WORKDIR /root/cyborgbot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/cyborgbot/bin:$PATH"

CMD ["python3", "-m", "cyborgbot"]
