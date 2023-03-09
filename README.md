# Uniandes Robotics Class

## Docker demos

In the docker folder, there are multiple ROS2 / Robotics demos based on a docker environment to play and interact.

These projects are based to be run in Ubuntu Linux, though the user can adapt them to their operating systems. The required dependencies for these are:

- [Docker](https://docs.docker.com/desktop/install/linux-install/)
- [Docker Nvidia Runtime](https://docs.docker.com/config/containers/resource_constraints/#gpu)
- [Nvidia Drivers](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html)

To run them, just open a new terminal and run the `setup.sh` script:

```bash
# Run nav2 docker demo
cd docker/nav2 && ./setup.sh
```
