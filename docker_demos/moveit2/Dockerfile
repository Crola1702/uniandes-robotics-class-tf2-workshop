FROM moveit/moveit2:humble-source AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV QT_X11_NO_MITSHM=1

WORKDIR /root/ws_moveit

RUN rm -rf src \
    && mkdir src \
    && cd src \
    && git clone https://github.com/ros-planning/moveit2_tutorials -b humble --depth 1 \
    && vcs import < moveit2_tutorials/moveit2_tutorials.repos

RUN apt update \
    && rosdep install -r --from-paths src --ignore-src --rosdistro $ROS_DISTRO -y \
    && apt clean

SHELL [ "/bin/bash", "-c" ]
RUN source /opt/ros/humble/setup.bash \
    && colcon build --mixin release --parallel-workers 2

RUN echo "source /root/ws_moveit/install/setup.bash" >> /root/.bashrc