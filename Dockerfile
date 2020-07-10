FROM pytorch/pytorch:1.5.1-cuda10.1-cudnn7-runtime

RUN apt-get update && apt-get install -y build-essential unzip wget

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

RUN wget https://ubisoft-model.s3.eu-west-3.amazonaws.com/newsgroup_data_encoded.zip --output-file=wget_log.txt
RUN wget https://ubisoft-model.s3.eu-west-3.amazonaws.com/model_weight.zip --output-file=wget_log_weight.txt
RUN unzip /app/newsgroup_data_encoded.zip
RUN unzip /app/model_weight.zip

COPY ./app /app
EXPOSE 9200

CMD ["python", "server.py"]
