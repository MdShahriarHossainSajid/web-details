#!/bin/bash

# Install Python 3.x
sudo apt-get update
sudo apt-get install -y python3

# Install required Python library
pip install python-whois

# Run the Python script
python3 website_details_viewer.py
