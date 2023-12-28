#!/usr/bin/env bash

# Install Python dependencies declared in requirements.txt
apt-get install -y python3 python3-pip python3-dev
pip3 install -r /autograder/source/requirements.txt

# Install valgrind memory tool
apt-get install valgrind -y

# Install Catch Framework for C++ testing
apt-get install catch -y

# Install cppcheck for static code analysis
apt-get install cppcheck -y