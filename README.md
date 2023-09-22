# ros_demo_module1
A demo module that includes two ROS 2 packages (listener/talker). It supports full containerization and a one-command setup and start using Docker compose. 

## Requirements
- Docker Engine
- Docker Compose plugin

## Setup
### 1. Clone the repository

### 2. Go into the repository's doccker directory and run docker compose up
```bash
cd ros_demo_module1/docker \
&& sudo docker compose up
```

The Docker image gets built and after that, compose will start up a container that automatically builds the colcon workspace and starts the launch file that was specified in `docker/ros_entrypoint.sh` which gets copied into the image during the build process.

You can stop the nodes at any time using `CTRL` + `C` in the command line. The compose will stop the container (it does not delete it!). This means, you can start the containter again using `sudo docker compose up`.

If you want to run the container detached, add the `-d` flag to the compose command like this:
```bash
sudo docker compose up -d
```

