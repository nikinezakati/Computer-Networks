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

s1 = net.addSwitch( 's1' )		

net.addLink(h1, s1, delay='47ms', cls=TCLink)
net.addLink(h2, s1, cls=TCLink)

net.start()

CLI(net)