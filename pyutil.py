#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import configparser
"""
Description: Imports logging and ConfigParser
"""
def init_and_get_config(config_file_name):
	config = None
	try:
		config = configparser.ConfigParser()
		config.read(config_file_name)
	except:
		logging.basicConfig(filename="debug.log",level=logging.DEBUG)
		logging.debug("Failed to import ConfigParser")
	else:
		if config.get("Logging", "Active").lower() == "true":
			mode = config.get("Logging", "Mode").lower()
			if mode == "debug":
				logging.basicConfig(filename="debug.log",level=logging.DEBUG)
			elif mode == "error":
				logging.basicConfig(filename="error.log",level=logging.ERROR)
	return config