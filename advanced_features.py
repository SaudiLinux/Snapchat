#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advanced Features for Snapchat User Information Extractor
Developed by: Saudi Linux
Email: SaudiLinux7@gmail.com
"""

import json
import time
import random
import socket
import requests
import os
from colorama import Fore, Style

class AdvancedFeatures:
    def __init__(self, auth_token=None):
        self.auth_token = auth_token
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Snapchat/10.88.0.69 (iPhone; iOS 14.4.2; gzip)",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}" if auth_token else ""
        }
    
    def set_auth_token(self, token):
        """Set authentication token"""
        self.auth_token = token
        self.headers["Authorization"] = f"Bearer {token}"
    
    def get_ip_info(self, ip_address):
        """Get information about an IP address"""
        try:
            print(f"\n{Fore.YELLOW}[*] Gathering IP information for: {ip_address}")
            
            # Simulate API request delay
            time.sleep(2)
            
            # This is simulated data - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            ip_data = {
                "ip": ip_address,
                "country": "United States",
                "region": "California",
                "city": "Los Angeles",
                "isp": "Example ISP",
                "latitude": "34.0522",
                "longitude": "-118.2437"
            }
            
            return ip_data
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to get IP information: {str(e)}")
            return None
    
    def display_ip_info(self, ip_data):
        """Display IP information in a formatted way"""
        if not ip_data:
            print(f"\n{Fore.RED}[!] No IP information available.")
            return
        
        try:
            print(f"\n{Fore.GREEN}[+] IP Information:")
            print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
            print(f"{Fore.CYAN}║ {Fore.WHITE}IP: {Fore.YELLOW}{ip_data.get('ip', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Country: {Fore.YELLOW}{ip_data.get('country', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Region: {Fore.YELLOW}{ip_data.get('region', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}City: {Fore.YELLOW}{ip_data.get('city', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}ISP: {Fore.YELLOW}{ip_data.get('isp', 'Unknown')}")
            
            latitude = ip_data.get('latitude', 'Unknown')
            longitude = ip_data.get('longitude', 'Unknown')
            print(f"{Fore.CYAN}║ {Fore.WHITE}Coordinates: {Fore.YELLOW}{latitude}, {longitude}")
            
            print(f"{Fore.CYAN}╚═══════════════════════════════════════════")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error displaying IP information: {str(e)}")
            return
    
    def get_account_security(self, username):
        """Check account security status"""
        try:
            print(f"\n{Fore.YELLOW}[*] Checking account security for: {username}")
            
            # Simulate API request delay
            time.sleep(2)
            
            # This is simulated data - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            security_data = {
                "username": username,
                "two_factor_enabled": random.choice([True, False]),
                "login_verification": random.choice([True, False]),
                "recovery_email": random.choice([True, False]),
                "recovery_phone": random.choice([True, False]),
                "last_password_change": "2023-01-01"
            }
            
            return security_data
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to check account security: {str(e)}")
            return None
    
    def display_security_info(self, security_data):
        """Display security information in a formatted way"""
        if not security_data:
            print(f"\n{Fore.RED}[!] No security information available.")
            return
        
        try:
            print(f"\n{Fore.GREEN}[+] Account Security Information:")
            print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Username: {Fore.YELLOW}{security_data['username']}")
            
            # Two-factor authentication status
            tfa_status = security_data.get('two_factor_enabled', False)
            tfa_color = Fore.GREEN if tfa_status else Fore.RED
            tfa_text = "Enabled" if tfa_status else "Disabled"
            print(f"{Fore.CYAN}║ {Fore.WHITE}Two-Factor Auth: {tfa_color}{tfa_text}")
            
            # Login verification status
            lv_status = security_data.get('login_verification', False)
            lv_color = Fore.GREEN if lv_status else Fore.RED
            lv_text = "Enabled" if lv_status else "Disabled"
            print(f"{Fore.CYAN}║ {Fore.WHITE}Login Verification: {lv_color}{lv_text}")
            
            # Recovery email status
            re_status = security_data.get('recovery_email', False)
            re_color = Fore.GREEN if re_status else Fore.RED
            re_text = "Set" if re_status else "Not Set"
            print(f"{Fore.CYAN}║ {Fore.WHITE}Recovery Email: {re_color}{re_text}")
            
            # Recovery phone status
            rp_status = security_data.get('recovery_phone', False)
            rp_color = Fore.GREEN if rp_status else Fore.RED
            rp_text = "Set" if rp_status else "Not Set"
            print(f"{Fore.CYAN}║ {Fore.WHITE}Recovery Phone: {rp_color}{rp_text}")
            
            print(f"{Fore.CYAN}║ {Fore.WHITE}Last Password Change: {Fore.YELLOW}{security_data.get('last_password_change', 'Unknown')}")
            print(f"{Fore.CYAN}╚═══════════════════════════════════════════")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error displaying security information: {str(e)}")
            return
    
    def get_account_activity(self, username):
        """Get account activity information"""
        try:
            print(f"\n{Fore.YELLOW}[*] Retrieving account activity for: {username}")
            
            # Simulate API request delay
            time.sleep(2)
            
            # This is simulated data - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            activity_data = {
                "username": username,
                "last_login": "2023-06-15 14:30:22",
                "login_ip": "192.168.1.1",
                "login_device": "iPhone 12 Pro",
                "recent_locations": [
                    {"city": "Los Angeles", "country": "USA", "timestamp": "2023-06-15 14:30:22"},
                    {"city": "New York", "country": "USA", "timestamp": "2023-06-10 09:15:45"},
                    {"city": "Chicago", "country": "USA", "timestamp": "2023-06-05 18:22:10"}
                ],
                "active_sessions": 2
            }
            
            return activity_data
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to get account activity: {str(e)}")
            return None
    
    def display_activity_info(self, activity_data):
        """Display activity information in a formatted way"""
        if not activity_data:
            print(f"\n{Fore.RED}[!] No activity information available.")
            return
        
        try:
            print(f"\n{Fore.GREEN}[+] Account Activity Information:")
            print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Username: {Fore.YELLOW}{activity_data.get('username', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Last Login: {Fore.YELLOW}{activity_data.get('last_login', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Login IP: {Fore.YELLOW}{activity_data.get('login_ip', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Login Device: {Fore.YELLOW}{activity_data.get('login_device', 'Unknown')}")
            print(f"{Fore.CYAN}║ {Fore.WHITE}Active Sessions: {Fore.YELLOW}{activity_data.get('active_sessions', 0)}")
            
            print(f"{Fore.CYAN}║ {Fore.WHITE}Recent Locations:")
            locations = activity_data.get('recent_locations', [])
            if locations:
                for i, location in enumerate(locations, 1):
                    city = location.get('city', 'Unknown')
                    country = location.get('country', 'Unknown')
                    timestamp = location.get('timestamp', 'Unknown')
                    print(f"{Fore.CYAN}║   {Fore.WHITE}{i}. {Fore.YELLOW}{city}, {country} - {timestamp}")
            else:
                print(f"{Fore.CYAN}║   {Fore.YELLOW}No recent locations found.")
            
            print(f"{Fore.CYAN}╚═══════════════════════════════════════════")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error displaying activity information: {str(e)}")
            return
            
    def track_active_location(self, username):
        """Track the active location of a target user"""
        try:
            print(f"\n{Fore.YELLOW}[*] Tracking active location for user: {username}")
            
            # Simulate API request delay
            time.sleep(2)
            
            # This is simulated data - in a real tool, you would make an actual API request
            # Note: This is for educational purposes only
            active_locations = [
                {
                    "device": "iPhone 12 Pro",
                    "app_version": "10.88.0.69",
                    "last_active": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "location": {
                        "city": "Dubai",
                        "country": "UAE",
                        "latitude": "25.2048",
                        "longitude": "55.2708",
                        "accuracy": "15m"
                    },
                    "connection_type": "WiFi",
                    "battery_level": "78%",
                    "is_charging": True
                },
                {
                    "device": "MacBook Pro",
                    "app_version": "Web 2.4.5",
                    "last_active": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 3600)),  # 1 hour ago
                    "location": {
                        "city": "Dubai",
                        "country": "UAE",
                        "latitude": "25.2048",
                        "longitude": "55.2708",
                        "accuracy": "50m"
                    },
                    "connection_type": "WiFi",
                    "is_charging": False
                }
            ]
            
            return active_locations
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to track active location: {str(e)}")
            return None
    
    def display_active_location(self, active_locations):
        """Display active location information in a formatted way"""
        if not active_locations:
            print(f"\n{Fore.RED}[!] No active location information available.")
            return
        
        try:
            print(f"\n{Fore.GREEN}[+] Active Location Tracking Information:")
            print(f"{Fore.CYAN}╔═══════════════════════════════════════════")
            
            for i, device_data in enumerate(active_locations, 1):
                device = device_data.get('device', 'Unknown Device')
                app_version = device_data.get('app_version', 'Unknown')
                last_active = device_data.get('last_active', 'Unknown')
                connection = device_data.get('connection_type', 'Unknown')
                battery = device_data.get('battery_level', 'Unknown')
                charging = "Yes" if device_data.get('is_charging', False) else "No"
                
                location = device_data.get('location', {})
                city = location.get('city', 'Unknown')
                country = location.get('country', 'Unknown')
                latitude = location.get('latitude', 'Unknown')
                longitude = location.get('longitude', 'Unknown')
                accuracy = location.get('accuracy', 'Unknown')
                
                print(f"{Fore.CYAN}║ {Fore.WHITE}Device {i}: {Fore.YELLOW}{device} ({app_version})")
                print(f"{Fore.CYAN}║ {Fore.WHITE}Last Active: {Fore.YELLOW}{last_active}")
                print(f"{Fore.CYAN}║ {Fore.WHITE}Location: {Fore.YELLOW}{city}, {country}")
                print(f"{Fore.CYAN}║ {Fore.WHITE}Coordinates: {Fore.YELLOW}{latitude}, {longitude} (±{accuracy})")
                print(f"{Fore.CYAN}║ {Fore.WHITE}Connection: {Fore.YELLOW}{connection}")
                
                if battery:
                    print(f"{Fore.CYAN}║ {Fore.WHITE}Battery: {Fore.YELLOW}{battery} (Charging: {charging})")
                
                if i < len(active_locations):
                    print(f"{Fore.CYAN}║ {Fore.WHITE}---")
            
            print(f"{Fore.CYAN}║ {Fore.WHITE}Map Link: {Fore.YELLOW}https://www.google.com/maps?q={latitude},{longitude}")
            print(f"{Fore.CYAN}╚═══════════════════════════════════════════")
            print(f"\n{Fore.GREEN}[+] You can copy the Map Link to view the location in Google Maps.")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error displaying active location information: {str(e)}")
            return
    
    def export_data_to_json(self, data, filename="snapchat_data.json"):
        """Export data to a JSON file"""
        if not data:
            print(f"{Fore.RED}[!] No data to export.")
            return False
            
        if not filename or not isinstance(filename, str):
            print(f"{Fore.RED}[!] Invalid filename provided.")
            return False
            
        try:
            # Create export directory if it doesn't exist
            export_dir = "exports"
            if not os.path.exists(export_dir):
                os.makedirs(export_dir)
                print(f"{Fore.GREEN}[+] Created export directory: {export_dir}")
                
            filepath = os.path.join(export_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"{Fore.GREEN}[+] Data exported to {filepath}")
            return True
        except FileNotFoundError:
            print(f"{Fore.RED}[!] Error: Path not found when exporting to {filename}")
            return False
        except PermissionError:
            print(f"{Fore.RED}[!] Error: Permission denied when exporting to {filename}")
            return False
        except json.JSONDecodeError:
            print(f"{Fore.RED}[!] Error: Invalid JSON data when exporting to {filename}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[!] Error exporting data: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    print(f"{Fore.YELLOW}[!] This module is not meant to be run directly.")
    print(f"{Fore.YELLOW}[!] Import it from the main script.")