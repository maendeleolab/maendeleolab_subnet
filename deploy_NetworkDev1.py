#!/usr/bin/python3

from maendeleolab_lib import *

#Public1 subnets
Public1_subnets_list=[
					  '10.7.1.0/24',#us-east-1
					  '10.110.1.0/24',#us-east-2
					 ]

#Public2 subnets
Public2_subnets_list=[
					  '10.7.2.0/24',#us-east-1
					  '10.110.2.0/24',#us-east-2
					 ]

#Private1 subnets
Private1_subnets_list=[
					  '10.7.8.0/24',#us-east-1
					  '10.110.8.0/24',#us-east-2
					 ]

#Private2 subnets
Private2_subnets_list=[
					  '10.7.9.0/24',#us-east-1
					  '10.110.9.0/24',#us-east-2
					 ]

#Availability zone 1
AZ1_list=[
		   'us-east-1a',
		   'us-east-2a',
	     ]

#Availability zone 2
AZ2_list=[
		   'us-east-1b',
		   'us-east-2b',
	     ]

Regions_list=[
			  'us-east-1',
			  'us-east-2',
			 ]

#Creates public subnets
for subnet, az, region in zip(Public1_subnets_list,AZ1_list,Regions_list):
	make_subnet(
				Subnet_name="NetworkDev1_Pub_1a",
				Vpc_Id=build_vpc.get_VpcId("NetworkDev1",region), 
				Tag_key="Type",
				Tag_value="not-billable",
				Cidr=subnet,#public1 subnets
				Availability_zone=az,
				Region=region
			 )

for subnet, az, region in zip(Public2_subnets_list,AZ2_list,Regions_list):
	make_subnet(
				Subnet_name="NetworkDev1_Pub_1b",
				Vpc_Id=build_vpc.get_VpcId("NetworkDev1",region), 
				Tag_key="Type",
				Tag_value="not-billable",
				Cidr=subnet,#public2 subnets
				Availability_zone=az,
				Region=region
			 )

#Create private subnets
for subnet, az, region in zip(Private1_subnets_list,AZ1_list,Regions_list):
	make_subnet(
				Subnet_name="NetworkDev1_Priv_1a",
				Vpc_Id=build_vpc.get_VpcId("NetworkDev1",region), 
				Tag_key="Type",
				Tag_value="not-billable",
				Cidr=subnet,#private1 subnets
				Availability_zone=az,
				Region=region
			 )

for subnet, az, region in zip(Private2_subnets_list,AZ2_list,Regions_list):
	make_subnet(
				Subnet_name="NetworkDev1_Priv_1b",
				Vpc_Id=build_vpc.get_VpcId("NetworkDev1",region), 
				Tag_key="Type",
				Tag_value="not-billable",
				Cidr=subnet,#private2 subnets
				Availability_zone=az,
				Region=region
			 )

# ----------------------------------- End -----------------------------------

