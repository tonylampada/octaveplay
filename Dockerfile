FROM ubuntu:14.04
RUN apt-get update --fix-missing
RUN apt-get install -y nano less octave python-pip
RUN apt-get install -y libblas-dev
RUN apt-get install -y liblapack-dev
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y gfortran
RUN apt-get install -y python-numpy
RUN apt-get install -y python-scipy
RUN apt-get install -y python-matplotlib
RUN apt-get install -y ipython
RUN apt-get install -y ipython-notebook
RUN apt-get install -y python-pandas
RUN apt-get install -y python-sympy
RUN apt-get install -y python-nose

WORKDIR /usr/src/app
RUN pip install numpy==1.11.0
RUN pip install scipy==0.17.0
RUN pip install oct2py==3.5.3

