from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController, Docker

def custom_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add SDN controller
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Add an SDN switch
    s1 = net.addSwitch('s1')

    # Add Docker containers with static ports
    d1 = net.addDocker('d1', ip='10.0.0.1', dimage="simple-web-server", ports=[8081], publish_all=True)
    d2 = net.addDocker('d2', ip='10.0.0.2', dimage="simple-web-server", ports=[8082], publish_all=True)

    # Create links between nodes
    net.addLink(d1, s1)
    net.addLink(d2, s1)

    # Start the network
    net.start()

    # Print the static URLs of the Docker containers
    print("\nStatic Docker Container URLs:")
    for i, container in enumerate(net.containers):
        port = container.ports[0]
        print(f'Container d{i+1}: http://localhost:{port}')

    # Connect switches to the controller
    s1.start([c0])

    # Run the command line interface
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    custom_topology()
