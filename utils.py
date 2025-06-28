#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility functions for Snapchat User Information Extractor
Developed by: Saudi Linux
Email: SaudiLinux7@gmail.com
"""

import re
import os
import sys
import json
import socket
import platform
from colorama import Fore, Style

def validate_username(username):
    """Validate Snapchat username format"""
    # Snapchat usernames can only contain letters, numbers, periods, hyphens, and underscores
    # They must be between 3 and 15 characters long
    pattern = r'^[a-zA-Z0-9._-]{3,15}$'
    if re.match(pattern, username):
        return True
    return False

def validate_email(email):
    """Validate email format"""
    # More comprehensive email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_ip_address(ip):
    """Validate IP address format"""
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    return False

def check_internet_connection():
    """Check if there is an active internet connection"""
    try:
        # Try to connect to multiple reliable servers with a timeout
        for host in ["www.google.com", "www.cloudflare.com", "www.microsoft.com"]:
            try:
                socket.create_connection((host, 80), timeout=3)
                return True
            except (socket.timeout, socket.gaierror, OSError):
                continue
        # If all connection attempts failed
        return False
    except Exception:
        return False

def get_system_info():
    """Get system information"""
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "python_version": platform.python_version(),
        "hostname": socket.gethostname()
    }
    return system_info

def display_system_info():
    """Display system information"""
    system_info = get_system_info()
    
    print(f"\n{Fore.GREEN}[+] System Information:")
    print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
    print(f"{Fore.CYAN}║ {Fore.WHITE}Operating System: {Fore.YELLOW}{system_info['os']}")
    print(f"{Fore.CYAN}║ {Fore.WHITE}OS Version: {Fore.YELLOW}{system_info['os_version']}")
    print(f"{Fore.CYAN}║ {Fore.WHITE}Architecture: {Fore.YELLOW}{system_info['architecture']}")
    print(f"{Fore.CYAN}║ {Fore.WHITE}Python Version: {Fore.YELLOW}{system_info['python_version']}")
    print(f"{Fore.CYAN}║ {Fore.WHITE}Hostname: {Fore.YELLOW}{system_info['hostname']}")
    print(f"{Fore.CYAN}╚═══════════════════════════════════════════")

def create_directory(directory):
    """Create a directory if it doesn't exist"""
    if not directory:
        print(f"{Fore.RED}[!] Error: No directory path provided.")
        return False
        
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Fore.GREEN}[+] Directory created: {directory}")
            return True
        else:
            print(f"{Fore.YELLOW}[*] Directory already exists: {directory}")
            return True
    except PermissionError:
        print(f"{Fore.RED}[!] Error: Permission denied when creating directory: {directory}")
        return False
    except OSError as e:
        print(f"{Fore.RED}[!] Error creating directory {directory}: {str(e)}")
        return False

def save_results(data, filename):
    """Save results to a file"""
    if not data:
        print(f"{Fore.RED}[!] No data to save.")
        return False
        
    if not filename or not isinstance(filename, str):
        print(f"{Fore.RED}[!] Invalid filename provided.")
        return False
        
    try:
        # Create results directory if it doesn't exist
        results_dir = "results"
        if not create_directory(results_dir):
            print(f"{Fore.RED}[!] Failed to create results directory.")
            return False
            
        filepath = os.path.join(results_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"{Fore.GREEN}[+] Results saved to {filepath}")
        return True
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: Path not found when saving to {filename}")
        return False
    except PermissionError:
        print(f"{Fore.RED}[!] Error: Permission denied when saving to {filename}")
        return False
    except json.JSONDecodeError:
        print(f"{Fore.RED}[!] Error: Invalid JSON data when saving to {filename}")
        return False
    except Exception as e:
        print(f"{Fore.RED}[!] Error saving results: {str(e)}")
        return False

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """Print a progress bar"""
    if total == 0:
        return
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        print()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
if __name__ == "__main__":
    print(f"{Fore.YELLOW}[!] This module is not meant to be run directly.")
    print(f"{Fore.YELLOW}[!] Import it from the main script.")