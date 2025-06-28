#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Snapchat User Information Extractor
Developed by: Saudi Linux
Email: SaudiLinux7@gmail.com
"""

import argparse
import sys
import os
import requests
import json
import time
import colorama
from colorama import Fore, Back, Style
from getpass import getpass

# Import custom modules
try:
    # Try to import from the current directory
    from utils import (
        validate_username, validate_email, validate_ip_address,
        check_internet_connection, display_system_info,
        save_results, print_progress_bar, clear_screen
    )
    from advanced_features import AdvancedFeatures
except ImportError as e:
    # Try to import using absolute path
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Add the script directory to the Python path
        sys.path.append(script_dir)
        
        # Try importing again
        from utils import (
            validate_username, validate_email, validate_ip_address,
            check_internet_connection, display_system_info,
            save_results, print_progress_bar, clear_screen
        )
        from advanced_features import AdvancedFeatures
    except ImportError as e:
        print(f"Error importing modules: {str(e)}")
        print("Make sure utils.py and advanced_features.py are in the same directory as this script.")
        sys.exit(1)

# Initialize colorama
colorama.init(autoreset=True)

# Banner
def print_banner():
    banner = f'''
    {Fore.YELLOW}╔═══════════════════════════════════════════════════╗
    {Fore.YELLOW}║                                                   ║
    {Fore.YELLOW}║   {Fore.RED}███████{Fore.YELLOW}╗{Fore.RED}███{Fore.YELLOW}╗   {Fore.RED}██{Fore.YELLOW}╗{Fore.RED}█████{Fore.YELLOW}╗ {Fore.RED}██████{Fore.YELLOW}╗ {Fore.RED}██████{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}╗  {Fore.RED}██{Fore.YELLOW}╗{Fore.RED}█████{Fore.YELLOW}╗ {Fore.RED}████████{Fore.YELLOW}╗   ║
    {Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}╔════╝{Fore.RED}████{Fore.YELLOW}╗  {Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}╔════╝{Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}╗╚══{Fore.RED}██{Fore.YELLOW}╔══╝   ║
    {Fore.YELLOW}║   {Fore.RED}███████{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}╔{Fore.RED}██{Fore.YELLOW}╗ {Fore.RED}██{Fore.YELLOW}║{Fore.RED}███████{Fore.YELLOW}║{Fore.RED}██████{Fore.YELLOW}╔╝{Fore.RED}██{Fore.YELLOW}║     {Fore.RED}███████{Fore.YELLOW}║{Fore.RED}███████{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║      ║
    {Fore.YELLOW}║   ╚════{Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║╚{Fore.RED}██{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}╔═══╝ {Fore.RED}██{Fore.YELLOW}║     {Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║      ║
    {Fore.YELLOW}║   {Fore.RED}███████{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║ ╚{Fore.RED}████{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║     {Fore.RED}██████{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║      ║
    {Fore.YELLOW}║   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ║
    {Fore.YELLOW}║                                                   ║
    {Fore.YELLOW}║   {Fore.GREEN}Snapchat User Information Extractor v1.0          {Fore.YELLOW}║
    {Fore.YELLOW}║   {Fore.CYAN}Developed by: Saudi Linux                          {Fore.YELLOW}║
    {Fore.YELLOW}║   {Fore.CYAN}Email: SaudiLinux7@gmail.com                       {Fore.YELLOW}║
    {Fore.YELLOW}╚═══════════════════════════════════════════════════╝
    '''
    print(banner)

# API endpoints
BASE_URL = "https://api.snapchat.com/v1"
LOGIN_URL = f"{BASE_URL}/login"
USER_INFO_URL = f"{BASE_URL}/user/info"

class SnapchatTool:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.user_agent = "Snapchat/10.88.0.69 (iPhone; iOS 14.4.2; gzip)"
        self.headers = {
            "User-Agent": self.user_agent,
            "Content-Type": "application/json"
        }
    
    def login(self, username, password):
        """Login to Snapchat and get authentication token"""
        if not username or not validate_username(username):
            print(f"{Fore.RED}[!] Invalid username format.")
            return False
            
        if not password or len(password) < 6:
            print(f"{Fore.RED}[!] Invalid password. Password must be at least 6 characters.")
            return False
            
        try:
            print(f"\n{Fore.YELLOW}[*] Attempting to login as {username}...")
            print(f"{Fore.YELLOW}[*] Connecting to authentication server...")
            
            # In a real implementation, this would use the actual Snapchat API
            # For demonstration purposes, we're simulating the login process
            
            # Simulate API request delay with progress bar
            for i in range(101):
                print_progress_bar(i, 100, prefix='Authenticating:', suffix='Complete', length=50)
                time.sleep(0.02)
            
            # This is a simulated response - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            print(f"{Fore.GREEN}[+] Login successful!")
            self.token = "simulated_auth_token"
            return True
            
        except ConnectionError:
            print(f"{Fore.RED}[!] Login failed: Unable to connect to authentication server.")
            return False
        except TimeoutError:
            print(f"{Fore.RED}[!] Login failed: Connection timed out.")
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Login failed: {str(e)}")
            return False
    
    def get_user_info(self, target_username):
        """Get information about a Snapchat user"""
        if not self.token:
            print(f"{Fore.RED}[!] Not authenticated. Please login first.")
            return None
        
        if not target_username or not validate_username(target_username):
            print(f"{Fore.RED}[!] Invalid target username.")
            return None
        
        try:
            print(f"\n{Fore.YELLOW}[*] Gathering information for user: {target_username}")
            print(f"{Fore.YELLOW}[*] Connecting to Snapchat servers...")
            
            # Simulate API request delay with progress bar
            for i in range(101):
                print_progress_bar(i, 100, prefix='Progress:', suffix='Complete', length=50)
                time.sleep(0.03)
            
            # This is simulated data - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            user_data = {
                "username": target_username,
                "email": f"{target_username}@example.com",  # Simulated email
                "ip_address": "192.168.1.1",  # Simulated IP
                "location": "Unknown",  # Simulated location
                "account_created": "2022-01-01",
                "last_active": "2023-01-01"
            }
            
            return user_data
            
        except ConnectionError:
            print(f"{Fore.RED}[!] Failed to connect to Snapchat servers. Check your internet connection.")
            return None
        except TimeoutError:
            print(f"{Fore.RED}[!] Connection timed out. Snapchat servers might be busy.")
            return None
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to get user information: {str(e)}")
            return None
    
    def display_user_info(self, user_data):
        """Display user information in a formatted way"""
        if not user_data:
            print(f"\n{Fore.RED}[!] No user information available.")
            return
        
        try:
            print(f"\n{Fore.GREEN}[+] User Information Found:")
            print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Username: {Fore.YELLOW}{user_data.get('username', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Email: {Fore.YELLOW}{user_data.get('email', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}IP Address: {Fore.YELLOW}{user_data.get('ip_address', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Location: {Fore.YELLOW}{user_data.get('location', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Account Created: {Fore.YELLOW}{user_data.get('account_created', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Last Active: {Fore.YELLOW}{user_data.get('last_active', 'Unknown')}")
            print(f"{Fore.CYAN}╚═══════════════════════════════════════════")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error displaying user information: {str(e)}")
            return

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Snapchat User Information Extractor")
    parser.add_argument("-u", "--username", help="Your Snapchat username")
    parser.add_argument("-t", "--target", help="Target Snapchat username")
    parser.add_argument("-a", "--advanced", action="store_true", help="Enable advanced features")
    parser.add_argument("-s", "--save", action="store_true", help="Save results to file")
    parser.add_argument("-c", "--check", action="store_true", help="Check system information")
    parser.add_argument("-v", "--version", action="version", version="Snapchat User Information Extractor v1.0")
    args = parser.parse_args()
    
    # Clear screen
    clear_screen()
    
    # Print banner
    print_banner()
    
    # Check internet connection
    print(f"{Fore.YELLOW}[*] Checking internet connection...")
    if not check_internet_connection():
        print(f"{Fore.RED}[!] No internet connection. Please check your network and try again.")
        return 1
    print(f"{Fore.GREEN}[+] Internet connection available.")
    
    # Display system information if requested
    if args.check:
        display_system_info()
    
    # Initialize tool
    tool = SnapchatTool()
    
    # Get login credentials
    username = args.username
    if not username:
        username = input(f"{Fore.YELLOW}[?] Enter your Snapchat username: ")
    
    # Validate username
    if not validate_username(username):
        print(f"{Fore.RED}[!] Invalid username format. Snapchat usernames must be 3-15 characters and can only contain letters, numbers, periods, hyphens, and underscores.")
        return 1
    
    password = getpass(f"{Fore.YELLOW}[?] Enter your Snapchat password: ")
    if not password or len(password) < 6:
        print(f"{Fore.RED}[!] Invalid password. Password must be at least 6 characters.")
        return 1
    
    # Login
    if not tool.login(username, password):
        return 1
    
    # Get target username
    target = args.target
    if not target:
        target = input(f"\n{Fore.YELLOW}[?] Enter target Snapchat username: ")
    
    # Validate target username
    if not validate_username(target):
        print(f"{Fore.RED}[!] Invalid target username format. Snapchat usernames must be 3-15 characters and can only contain letters, numbers, periods, hyphens, and underscores.")
        return 1
    
    # Get and display user information
    print(f"{Fore.YELLOW}[*] Retrieving user information...")
    user_info = tool.get_user_info(target)
    tool.display_user_info(user_info)
    
    # Advanced features if requested
    if args.advanced and user_info:
        print(f"\n{Fore.YELLOW}[*] Enabling advanced features...")
        advanced = AdvancedFeatures(tool.token)
        
        # Get IP information
        print(f"{Fore.YELLOW}[*] Retrieving IP information...")
        ip_info = advanced.get_ip_info(user_info['ip_address'])
        advanced.display_ip_info(ip_info)
        
        # Get account security information
        print(f"{Fore.YELLOW}[*] Retrieving security information...")
        security_info = advanced.get_account_security(target)
        advanced.display_security_info(security_info)
        
        # Get account activity information
        print(f"{Fore.YELLOW}[*] Retrieving activity information...")
        activity_info = advanced.get_account_activity(target)
        advanced.display_activity_info(activity_info)
        
        # Combine all data
        all_data = {
            "user_info": user_info,
            "ip_info": ip_info,
            "security_info": security_info,
            "activity_info": activity_info,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save results if requested
        if args.save:
            filename = f"{target}_data_{time.strftime('%Y%m%d_%H%M%S')}.json"
            if save_results(all_data, filename):
                print(f"{Fore.GREEN}[+] All data saved successfully to {filename}!")
            else:
                print(f"{Fore.RED}[!] Failed to save data to {filename}.")
    elif args.save and user_info:
        # Save basic results if requested
        filename = f"{target}_basic_data_{time.strftime('%Y%m%d_%H%M%S')}.json"
        if save_results(user_info, filename):
            print(f"{Fore.GREEN}[+] Basic data saved successfully to {filename}!")
        else:
            print(f"{Fore.RED}[!] Failed to save data to {filename}.")
    
    print(f"\n{Fore.GREEN}[+] Operation completed successfully!")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operation cancelled by user.")
    except ConnectionError:
        print(f"\n{Fore.RED}[!] Connection error: Unable to connect to the server.")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}[!] Network error: {str(e)}")
    except json.JSONDecodeError:
        print(f"\n{Fore.RED}[!] Error: Invalid JSON response from server.")
    except FileNotFoundError as e:
        print(f"\n{Fore.RED}[!] File error: {str(e)}")
    except PermissionError as e:
        print(f"\n{Fore.RED}[!] Permission error: {str(e)}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] An unexpected error occurred: {str(e)}")
    finally:
        print(f"\n{Fore.YELLOW}[*] Exiting...")
        sys.exit(0)