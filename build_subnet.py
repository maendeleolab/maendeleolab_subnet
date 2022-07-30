#!/usr/bin/python3

Goal = '''
to create subnet/s in aws
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
									filename=FPATH+'/maendeleolab_subnet/subnet.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
        return name # e.g: 'us-east-1'

#create instance
def make_subnet(**kwargs):
	''' Creates subnet in a specific region and availability zone '''
	try:
		os.system("aws ec2 create-subnet \
			--tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=" + kwargs['Subnet_name'] + "},\
								  {Key=" + kwargs['Tag_key'] + ",Value=" + kwargs['Tag_value'] + "}]'\
			--vpc-id " + kwargs['Vpc_Id'] + "\
			--cidr-block " + kwargs['Cidr'] + "\
			--availability-zone " + kwargs['Availability_zone'] + "\
			--region " + kwargs['Region'] 
		)
		logging.info('Created VPC:' + kwargs['Subnet_name'])
	except Exception as err:
		logging.info(err)
		print(err)

def get_SubnetId(subnet_name, region='us-east-1'):
	try:
		''' Gets resource id from json output and can be used in deploy scripts '''
		output = os.popen('aws ec2 describe-subnets --filters Name=tag:Name,Values=' + subnet_name + ' --region '+ region).read()
		subnet_data = json.loads(str(output))
		data = subnet_data['Subnets'][0]['SubnetId']
		return data
	except Exception as err:
		print('Logging get_SubnetId to subnet.log')
		logging.info(err)

def destroy_subnet(Subnet_id, region='us-east-1'):
	try:
		os.system("aws ec2 delete-subnet --subnet-id " + Subnet_id + ' --region '+ region)
	except Exception as err:
		print('Logging destroy_subnet to subnet.log')
		logging.info(err)

def erase_subnets(region='us-east-1'):
	try:
		''' Deletes all subnets that do not have any dependencies '''
		output = os.popen('aws ec2 describe-subnets  --region ' + region).read()
		subnet_data = json.loads(str(output))
		for data in subnet_data['Subnets']:
			for item in data['Tags']:
				print('Logging: '+ data['SubnetId'])
				destroy_subnet(data['SubnetId'], region)
				logging.info('Logging: ' + data['SubnetId'])
	except Exception as err:
		logging.info(err)
		print('Logging error to subnet.log')

# ------------------------------------------------- End ------------------------------------------------------
