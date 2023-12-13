#!/bin/bash

# Exit on error
set -e

sudo apt update
# Required for dask visualzation
sudo apt install -y graphviz 

# Python depdencies
python -m pip install -r requirements.txt

# gcloud command
cd ~
curl -LO https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-457.0.0-linux-x86_64.tar.gz
tar xzf google-cloud-cli-457.0.0-linux-x86_64.tar.gz
rm google-cloud-cli-457.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh  --quiet
echo 'PATH="${HOME}/google-cloud-sdk/bin:${PATH}"' >> ~/.bashrc

# Set prompt
echo 'PS1="$ "' >> ~/.bashrc
