# SDN-SingleTopo-Project
# Demonstrate container-based images on SDN.
# Step 1: Install Mininet and Docker
# Step 2: Create a Docker Container
#   (Use the Dockerfile file provided)
#   -Build the Docker image:
#             $docker build -t simple-web-server:1.0 .
#             $docker images
#             $docker tag "simple-web-server:1.0" "your_username/simple-web-server:1.0"
#   -Ship the Docker image
#             $docker login
#             $docker push "your_username/simple-web-server:1.0"
#             Verify in Dockerhub
#   -Run the Docker image
#             $docker run simple-web-server:1.0
# Step 3: Create a Mininet Topology
#   (Use the sdn_topology.py provided)
# Step 4: Run the Topology
#         Run the Mininet topology script: sudo python3 sdn_topology.py
#         (This will start the Mininet environment with an SDN switch and two Docker containers connected to it. The containers are running a basic Nginx web server.)

