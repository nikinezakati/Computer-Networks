#!/usr/bin/env python
from mininet.net import Mininet
from mininet.link import TCIntf
from mininet.node import CPULimitedHost 
from mininet.topolib import TreeTopo 
from mininet.util import custom, quietRun 
from mininet.log import setLogLevel, info 
from mininet.cli import CLI
from mininet.node import RemoteController 
from mininet.link import TCLink
import os


setLogLevel( 'info' )

net = Mininet( link=TCLink )
c0 = net.addController(name='c0')

# Your network logic is here 
h1 = net.addHost( 'h1' )		
h2 = net.addHost( 'h2' )		

s2 = net.addSwitch( 's2' )

net.addLink(h2, s2, bw=188, cls=TCLink)
net.addLink(h1, s2, cls=TCLink)

net.start()

CLI(net)