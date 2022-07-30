#!/usr/bin/env python3

import os, json
from build_subnet import destroy_subnet, erase_subnets

maendeleolab_infra=['us-east-1','us-east-2']

for region in maendeleolab_infra:
	erase_subnets(region)

# --------------------- End -------------------------
