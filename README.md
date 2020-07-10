# News Predictor API

## Setup

```
sudo docker build -t newspredictor
```

```
sudo docker run -it -e port:9200 -p 9200:9200 --rm newspredictor
```

This will run the application on localhost:9200

## Usage example

```
curl -X POST -d @tests/test_mideast.txt  127.0.0.1:9200/predict
```
```
curl -X POST -d @tests/test_guns.txt  127.0.0.1:9200/predict
```
```
curl -X POST -d @tests/test_autos.txt  127.0.0.1:9200/predict
```
```
curl -X POST -d @tests/test_christian.txt  127.0.0.1:9200/predict
```