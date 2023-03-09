FROM ros:humble-ros-base AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV QT_X11_NO_MITSHM=1

# Install / update tools
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    git \
    gnupg2 \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install tf2 packages
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    ros-humble-turtle-tf2-py \
    ros-humble-tf2-tools \
    ros-humble-tf-transformations\
    && rm -rf /var/lib/apt/lists/*  

WORKDIR /root/turtle_tf2_ws
