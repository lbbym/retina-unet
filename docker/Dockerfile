ARG cuda_version=8.0
ARG cudnn_version=6
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    apt-get update && \
    apt-get install -y wget git libhdf5-dev g++ graphviz openmpi-bin libgl1 && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.3.27-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash /miniconda.sh -f -b -p $CONDA_DIR && \
    rm miniconda.sh

ENV NB_USER keras
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown keras $CONDA_DIR -R && \
    mkdir -p /src && \
    chown keras /src

USER keras

# Python
ARG python_version=3.5

RUN conda install -y python=${python_version} && \
    pip install --upgrade pip && \
    #pip install tensorflow-gpu && \  #uncomment to install tensorflow support
    #pip install https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp35-cp35m-linux_x86_64.whl && \ #uncomment to install CNTK support
    conda install Pillow scikit-learn notebook pandas matplotlib mkl nose pyyaml six h5py && \
    conda install theano pygpu bcolz && \
    pip install sklearn_pandas && \
    pip install git+git://github.com/fchollet/keras.git && \
    conda clean -yt

RUN conda install -c menpo opencv3 && \
    pip install opencv-python

RUN git clone git://github.com/alevalv/retina-unet.git /src

ADD theanorc /home/keras/.theanorc

ADD kerasrc /home/keras/.keras/keras.json

RUN chown /home/keras/.theanorc && \
    chown /home/keras/.keras/keras.json

ENV PYTHONPATH='/src/:$PYTHONPATH'

WORKDIR /src
