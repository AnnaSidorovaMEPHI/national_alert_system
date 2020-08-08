#!/usr/bin/env python
import smtplib
import sys
import json
import os

class EmailSender(object):
	"""docstring for EmailSender"""
	def __init__(self, addresses = []):
		self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
		self.addresses = addresses

	def send_alert(self, text):
		if self.addresses:
			self.smtp.starttls()
			conf = self._load_json(".\\src\\config.json")
			login = conf["login"]
			password = conf["password"]
			self.smtp.login(login, password)
			self.smtp.sendmail(login, self.addresses, text)
			self.smtp.quit()
		else:
			sys.stdout.write("Can not send email to" + str(addresses))

	@staticmethod	
	def _load_json(path):
		abs_path = path
		with open(abs_path, "rb") as json_file:
			data = json.loads(json_file.read())
		return data



