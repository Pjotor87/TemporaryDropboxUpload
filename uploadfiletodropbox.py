#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyutil
config = pyutil.init_and_get_config("pyconfig.txt")
import requests
import json
import time
"""
Description: Uploads a file to dropbox, waits for a short while, and then deletes that same uploaded file
"""

def upload_file_to_dropbox():
	pyutil.logging.debug("Uploading file to dropbox...")
	headers = {
		"Authorization": "Bearer " + config.get("Dropbox", "access_token"),
		"Content-Type": "application/octet-stream",
		"Dropbox-API-Arg": "{\"path\":\"" + config.get("Dropbox", "target_filepath") + "\"}"
	}
	data = open(config.get("Dropbox", "source_filepath"), "rb").read()
	r = requests.post(config.get("Dropbox", "dropbox_api_upload_endpont"), headers=headers, data=data)
	pyutil.logging.debug("File uploaded!")

def wait_for_a_while():
	import_time_in_seconds = int(config.get("Dropbox", "import_time_in_seconds"))
	pyutil.logging.debug("Waiting for {0} seconds...".format(import_time_in_seconds))
	time.sleep(import_time_in_seconds)
	
def delete_file_from_dropbox():
	pyutil.logging.debug("Deleting file from dropbox...")
	headers = {
		"Authorization": "Bearer " + config.get("Dropbox", "access_token"),
		"Content-Type": "application/json"
	}
	data = { "path": config.get("Dropbox", "target_filepath") }
	r = requests.post(config.get("Dropbox", "dropbox_api_delete_endpont"), headers=headers, data=json.dumps(data))
	pyutil.logging.debug("File deleted!")

def main():
	try:
		upload_file_to_dropbox()
		wait_for_a_while()
		delete_file_from_dropbox()
	except Exception as e:
		pyutil.logging.error(e)
        
if __name__ == "__main__":
    main()