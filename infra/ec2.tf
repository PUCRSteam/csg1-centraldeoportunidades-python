resource "aws_instance" "csg1-central-oportunidades" {
  ami           = "ami-007855ac798b5175e" # Ubuntu 22.04 LTS
  instance_type = "t2.micro"
  subnet_id = element(module.vpc.private_subnets, 0)
  tags = {
    Name = "terraform-csg1-instance"
  }
}