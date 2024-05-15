
from diagrams import Diagram, Cluster
from diagrams.aws.network import ELB
from diagrams.aws.compute import EC2

with Diagram("Web Server Architecture", show=False):
    with Cluster("Web Servers"):
        web_server_1 = EC2("Web Server 1")
        web_server_2 = EC2("Web Server 2")
        web_server_3 = EC2("Web Server 3")

    load_balancer = ELB("Load Balancer")

    load_balancer >> [web_server_1, web_server_2, web_server_3]
