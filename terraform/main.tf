terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

data "aws_instance" "library_server" {
  filter {
    name   = "tag:Name"
    values = ["library-management-platform"]
  }

  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}

output "library_instance_id" {
  description = "ID of the existing library management EC2 instance"
  value       = data.aws_instance.library_server.id
}

output "library_public_ip" {
  description = "Public IP of the existing library management EC2 instance"
  value       = data.aws_instance.library_server.public_ip
}
