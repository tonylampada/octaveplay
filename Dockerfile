FROM python:2.7
RUN apt-get update
RUN apt-get install -y nano octave
RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
RUN pip install uwsgi
RUN pip install uwsgitop

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
