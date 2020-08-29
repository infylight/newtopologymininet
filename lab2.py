
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
net = Mininet(link =TCLink)
# need to create controller 11 hosts  and  4 switches 
#controllers
c0 = net.addController()
#hosts
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
h6 = net.addHost('h6')
h7 = net.addHost('h7')
h8 = net.addHost('h8')
h9 = net.addHost('h9')
h10 = net.addHost('h10')
h0 = net.addHost('h0')
#switches 
s0 = net.addSwitch('s0')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')

#creating links between the nodes and switches 

net.addLink(h0,s3, bw =2 ,d = '3ms')
net.addLink(h1,s0, bw =3 ,d = '4ms')
net.addLink(h2,s0, bw =2.5 ,d= '10ms')
net.addLink(h3,s1, bw =1.5 ,d = '19ms')
net.addLink(h4,s1, bw =4.5 ,d = '25ms')
net.addLink(h5,s1, bw =1 ,d = '9ms')
net.addLink(h6,s2, bw =5 ,d= '20ms')
net.addLink(h7,s2, bw =2 ,d = '22ms')
net.addLink(h8,s3, bw =10 ,d = '7ms')
net.addLink(h9,s3, bw =10 ,d = '6ms')
net.addLink(h10,s2, bw =10 ,d = '19ms')
net.addLink(s0,s1)
net.addLink(s1,s2)
net.addLink(s2,s3)

#setting ip's
h0.setIP('10.0.0.1')
h1.setIP('10.0.0.2')
h2.setIP('10.0.0.3')
h3.setIP('10.0.0.4')
h4.setIP('10.0.0.5')
h5.setIP('10.0.0.6')
h6.setIP('10.0.0.7')
h7.setIP('10.0.0.8')
h8.setIP('10.0.0.9')
h9.setIP('10.0.0.10')
h10.setIP('10.0.0.11')




net.start()
#net.pingAll()
#dumpNodeConnections(net.hosts)
#net.links()

CLI(net)
net.stop()


