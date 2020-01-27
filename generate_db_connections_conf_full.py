#!/usr/bin/python

import csv
import os
from jinja2 import Template
from jinja2.utils import Namespace

path = os.getcwd()
db_connection_path=path+"\db_connections.conf"
db_inputs_path=path+"\db_inputs.conf"

def createConnectionsConf(obj,inputsPath):
	connectionsConf = '''
[connection_for_{{ obj[0] }}]
connection_type = {{ obj[3] }}
database = {{ obj[2] }}
disabled = {{ obj[4] }}
host = {{ obj[0] }}
identity = {{ obj[5] }}
jdbcUseSSL = {{ obj[6] }}
localTimezoneConversionEnabled = {{ obj[7] }}
port = {{ obj[1] }}
readonly = {{ obj[8] }}
timezone = {{ obj[9] }}

	'''
	file = open(inputsPath,"a")
	connections = Template(connectionsConf)
	output=connections.render(obj=obj)
	file.write(output)
	file.close()
	
def createInputsConf(obj,inputsPath):
	connectionsConf = '''
[InputOracleDB_{{ obj[0] }}]
batch_upload_size = {{ obj[10] }}
connection = connection_for_{{ obj[0] }}
description = {{ obj[11] }}
disabled = {{ obj[12] }}
fetch_size = {{ obj[13] }}
index = {{ obj[14] }}
index_time_mode = {{ obj[15] }}
input_timestamp_column_number = {{ obj[16] }}
interval = {{ obj[17] }}
max_rows = {{ obj[18] }}
max_single_checkpoint_file_size = {{ obj[19] }}
mode = {{ obj[20] }}
query = {{ obj[21] }}
query_timeout = {{ obj[22] }}
sourcetype = {{ obj[23] }}
tail_rising_column_number = {{ obj[24] }}
template_name = {{ obj[25] }}

	'''
	file = open(inputsPath,"a")
	connections = Template(connectionsConf)
	output=connections.render(obj=obj)
	file.write(output)
	file.close()


with open('inputs_full.csv') as ifile:
	read = csv.reader(ifile,delimiter=';') 
	objectHeader = next(read)
	for row in read:
		createConnectionsConf(row,db_connection_path)
		createInputsConf(row,db_inputs_path)