#!/usr/bin/env python3

from maendeleolab_lib import *

#public1 subnets
Public1_subnets_list=[
    '10.7.1.0/24',#us-east-1
    '10.107.1.0/24',#us-west-2
    ]

#public2 subnets
Public2_subnets_list=[
    '10.7.2.0/24',#us-east-1
    '10.107.2.0/24',#us-west-2
    ]

#private1 subnets
Private1_subnets_list=[
    '10.7.8.0/24',#us-east-1
    '10.107.8.0/24',#us-west-2
    ]

#private2 subnets
Private2_subnets_list=[
    '10.7.9.0/24',#us-east-1
    '10.107.9.0/24',#us-west-2
    ]

#availability zone 1
AZ1_list=[
    'us-east-1a', #Availability zone 1 in us-east-1
    'us-west-2a', #Availability zone 1 in us-west-2
    ]

#availability zone 2
AZ2_list=[
    'us-east-1b', #Availability zone 2 in us-east-1
    'us-west-2b', #Availability zone 2 in us-west-2
    ]

Regions_list=[
    'us-east-1',
    'us-west-2',
    ]

#create public subnet 1
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

#create public subnet 2
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

#Create private subnet 1
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

#Create private subnet 2
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


