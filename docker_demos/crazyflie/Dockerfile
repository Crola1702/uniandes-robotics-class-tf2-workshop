FROM ubuntu:focal AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV QT_X11_NO_MITSHM=1

WORKDIR /home/ws_crazyflie

RUN apt update \
    && apt install -y \
    build-essential \
    freeglut3-dev \
    git \
    gnupg2 \ 
    libglu1-mesa-dev \
    libgmp-dev \
    libx11-dev \ 
    mesa-common-dev \
    wget \
    && rm -r /var/lib/apt/lists/*

# Install Conda, used to install Safe Gym
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda.sh \
    && /bin/bash ./miniconda.sh -b -p /opt/conda \
    && rm miniconda.sh
ENV PATH /opt/conda/bin:$PATH

# Set conda environment
RUN pip install --upgrade pip \
    && conda init bash \
    && conda create -n safe python=3.8.10 -y 

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "safe", "/bin/bash", "-c"]

RUN git clone https://github.com/utiasDSL/safe-control-gym.git --depth 1 \
    && cd safe-control-gym \
    && pip install casadi \
    && pip install -e .

ENTRYPOINT ["conda", "run", "-n", "safe"]
