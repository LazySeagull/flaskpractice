from flask import Flask
from configparser import ConfigParser

config = ConfigParser()
config.read('flaskkipracticekrlo/config.cfg')
api_key = config.get('API','api_key')

print(api_key)

