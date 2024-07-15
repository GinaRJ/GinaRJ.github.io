import pytest
import os
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def test_diagram_creation():
    with Diagram("WebExample", show=False):
        lb = ELB("lb")
        web = EC2("web")
        userdb = RDS("userdb")

        assert lb is not None
        assert web is not None
        assert userdb is not None

def test_diagram_connections():
    with Diagram("WebExample", show=False):
        lb = ELB("lb")
        web = EC2("web")
        userdb = RDS("userdb")

        assert lb >> web
        assert web >> userdb

def test_diagram_generation():
	with Diagram("WebExample", show=False):
		lb = ELB("lb")
		web = EC2("web")
		userdb = RDS("userdb")

		lb >> web >> userdb

def test_png_generation():
    diagram_path = "WebExample.png"
    with Diagram("WebExample", show=False, filename="WebExample"):
        lb = ELB("lb")
        web = EC2("web")
        lb >> web

    # Check that the diagram is generated and saved in the right directory
    assert os.path.exists(diagram_path), "Diagram file does not exist"

    # Clean up: remove the generated file
    os.remove(diagram_path)
