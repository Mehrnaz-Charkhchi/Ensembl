FROM python:3
RUN mkdir /ensembl;
WORKDIR /ensembl

ADD requirements.pip /ensembl
RUN pip install -r /ensembl/requirements.pip
