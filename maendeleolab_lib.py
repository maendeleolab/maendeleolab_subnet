#!/usr/bin/python3

import os, json, sys, pprint, itertools
from build_subnet import region_id, make_subnet
from build_subnet import destroy_subnet, erase_subnets
FPATH = os.environ.get('ENV_FPATH') #ENV_FPATH should be set in your environment variable file
sys.path.append(FPATH+'/cloudNetworkSpecialty/vpc')
import build_vpc

# ----------------- End -----------------------
