from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

#filenamePrefix = "diagram_"
#filenameNumber[]
with Diagram("WebExample", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
#    filenameNumber.append((len)filenameNumber + 1)

# maybe have a list to append the names of the diagrams to?
# then use that name for the diagram image file name
# make a diagram of this project lol
# make diagrams save in generated_diagrams folder

with Diagram("Simple Diagram", show=False):
    EC2("web") >> RDS("your mom")
