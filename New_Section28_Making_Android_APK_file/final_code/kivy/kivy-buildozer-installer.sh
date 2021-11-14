#!/bin/bash

# Install Python pip
sudo apt-get install -y curl
sudo apt-get install -y python3-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py

# Dependencies with SDL2
# Install necessary system packages
sudo apt-get install -y python3-pip
sudo apt-get install -y build-essential
sudo apt-get install -y git
sudo apt-get install -y python
sudo apt-get install -y python3-dev
sudo apt-get install -y ffmpeg
sudo apt-get install -y libsdl2-dev
sudo apt-get install -y libsdl2-image-dev
sudo apt-get install -y libsdl2-mixer-dev 
sudo apt-get install -y libsdl2-ttf-dev
sudo apt-get install -y libportmidi-dev
sudo apt-get install -y libswscale-dev
sudo apt-get install -y libavformat-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y libavcodec-dev

# Dependencies Kivy
sudo pip3 install cython

# Install Kivy
sudo pip3 install kivy

# Dependencies Buildozer
sudo apt-get install -y build-essential 
sudo apt-get install -y ccache 
sudo apt-get install -y git 
sudo apt-get install -y libncurses5:i386 
sudo apt-get install -y libstdc++6:i386 
sudo apt-get install -y libgtk2.0-0:i386 
sudo apt-get install -y libpangox-1.0-0:i386 
sudo apt-get install -y libpangoxft-1.0-0:i386 
sudo apt-get install -y libidn11:i386 
sudo apt-get install -y python2.7 
sudo apt-get install -y python2.7-dev 
sudo apt-get install -y openjdk-8-jdk 
sudo apt-get install -y unzip 
sudo apt-get install -y zlib1g-dev 
sudo apt-get install -y zlib1g:i386 
sudo apt-get install -y libltdl-dev 
sudo apt-get install -y libffi-dev 
sudo apt-get install -y libssl-dev 
sudo apt-get install -y autoconf 
sudo apt-get install -y autotools-dev
sudo apt-get install -y cmake
sudo apt-get install -y zip

# Install Buildozer

# Cloning Buildozer repository directly to the HOME directory causes the
# AttributeError 'Namespace' object has no attribute 'ignore_setup_py' error when trying to build apk file.
# So Buildozer repository should be cloned to any directory except HOME
mkdir ~/buildozer-repo
cd ~/buildozer-repo

git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python3 setup.py install
