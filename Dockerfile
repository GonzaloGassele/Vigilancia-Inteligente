FROM python:3.8

RUN apt-get update && apt-get install -y

RUN pip install --upgrade pip

RUN pip install opencv-contrib-python-headless \
    pip install pywhatkit \
    && pip install vidgear

WORKDIR /system

COPY . .

RUN pip install -r requirements.txt

CMD ["model.py"]

ENTRYPOINT [ "python3" ]