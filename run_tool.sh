#!/bin/bash

echo "===================================="
echo "Snapchat User Information Extractor"
echo "===================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 using your package manager:"
    echo "  - For Debian/Ubuntu: sudo apt install python3 python3-pip"
    echo "  - For Fedora: sudo dnf install python3 python3-pip"
    echo "  - For Arch Linux: sudo pacman -S python python-pip"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d" " -f2)
echo "Found Python version: $PYTHON_VERSION"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install pip for Python 3 and try again."
    exit 1
fi

# Check internet connection
echo "Checking internet connection..."
if ! ping -c 1 google.com &> /dev/null && ! ping -c 1 cloudflare.com &> /dev/null; then
    echo "Error: No internet connection detected. Please check your connection and try again."
    exit 1
fi

# Install required packages
echo "Installing required packages..."
python3 -m pip install -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to install required packages."
    echo "Possible solutions:"
    echo "  1. Check your internet connection"
    echo "  2. Try running: python3 -m pip install --upgrade pip"
    echo "  3. Try running with sudo: sudo python3 -m pip install -r requirements.txt"
    exit 1
fi

# Make the script executable
echo "Setting execution permissions..."
chmod +x snapchat_tool.py

if [ $? -ne 0 ]; then
    echo "Warning: Failed to set execution permissions. Continuing anyway..."
fi

# Run the tool
echo "Starting Snapchat User Information Extractor..."
python3 snapchat_tool.py

# Check if tool execution was successful
if [ $? -ne 0 ]; then
    echo "Error: Tool execution failed. Please check the error messages above."
    exit 1
fi