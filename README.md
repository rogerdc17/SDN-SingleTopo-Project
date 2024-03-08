# SDN SingleTopo Project

This project demonstrates the integration of container-based images with Software-Defined Networking (SDN). Follow the steps below to set up and run the project.

## Step 1: Install Mininet and Docker

Make sure to have Mininet and Docker installed on your system.

## Step 2: Create a Docker Container

Use the provided Dockerfile to build a Docker image for a simple web server.
Build the Docker image:
```bash
$ docker build -t simple-web-server:1.0 .
$ docker images
$ docker tag simple-web-server:1.0 your_username/simple-web-server:1.0
```
Ship the Docker image to Docker Hub:
```bash
$ docker login
$ docker push your_username/simple-web-server:1.0
```
Verify the image on Docker Hub.
Run the Docker image:
```bash
$ docker run simple-web-server:1.0
```

## Step 3: Create a Mininet Topology

Utilize the sdn_topology.py script to define the SDN topology.

## Step 4: Run the Topology

Execute the Mininet topology script:
```bash
$ sudo python3 sdn_topology.py
```
Adjust your web browser accordingly to access the web servers using the static URLs:

```Container 1:
http://localhost:8081
```
```Container 2:
http://localhost:8082
```
