resource "aws_security_group" "sc-csg1" {
  name   = "scg-csg1"
  vpc_id = module.vpc.vpc_id

  ingress = [
    {
       cidr_blocks = [
        "0.0.0.0/0",
       ]
       description      = "ssh"
       from_port        = 22
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "tcp"
       security_groups  = []
       self             = false
       to_port          = 22
    },
    {
       cidr_blocks = [
        "0.0.0.0/0",
       ]
       description      = "https"
       from_port        = 443
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "tcp"
       security_groups  = []
       self             = false
       to_port          = 443
    },
    {
       cidr_blocks = [
        "0.0.0.0/0",
       ]
       description      = "app"
       from_port        = 8080
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "tcp"
       security_groups  = []
       self             = false
       to_port          = 8080
    },
    {
       cidr_blocks = [
        "0.0.0.0/0",
       ]
       description      = "web hosting"
       from_port        = 80
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "tcp"
       security_groups  = []
       self             = false
       to_port          = 80
    },
    {
       cidr_blocks = [
         "0.0.0.0/0",
       ]
       description      = "icmpv4"
       from_port        = -1
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "icmp"
       security_groups  = []
       self             = false
       to_port          = -1
    },
   ]
  
  egress  = [
    {
       cidr_blocks = [
        "0.0.0.0/0",
       ]
       description      = ""
       from_port        = 0
       ipv6_cidr_blocks = []
       prefix_list_ids  = []
       protocol         = "-1"
       security_groups  = []
       self             = false
       to_port          = 0
    },
  ]
}