FROM python:2.7
RUN apt-get update --fix-missing
RUN apt-get install -y nano octave
RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

WORKDIR /usr/src/app
RUN pip install numpy==1.11.0
RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
RUN pip install scipy==0.17.0
RUN pip install oct2py==3.5.3
