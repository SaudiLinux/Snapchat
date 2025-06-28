#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for Snapchat User Information Extractor
Developed by: Saudi Linux
Email: SaudiLinux7@gmail.com
"""

import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import modules to test
try:
    from utils import (
        validate_username, validate_email, validate_ip_address,
        check_internet_connection, get_system_info
    )
    from advanced_features import AdvancedFeatures
    from snapchat_tool import SnapchatTool
except ImportError as e:
    print(f"Error importing modules: {str(e)}")
    print("Make sure utils.py, advanced_features.py, and snapchat_tool.py are in the same directory.")
    sys.exit(1)

class TestUtils(unittest.TestCase):
    """Test utility functions"""
    
    def test_validate_username(self):
        """Test username validation"""
        # Valid usernames
        self.assertTrue(validate_username("user123"))
        self.assertTrue(validate_username("user.name"))
        self.assertTrue(validate_username("user_name"))
        self.assertTrue(validate_username("user-name"))
        
        # Invalid usernames
        self.assertFalse(validate_username("us"))  # Too short
        self.assertFalse(validate_username("username123456789012"))  # Too long
        self.assertFalse(validate_username("user@name"))  # Invalid character
        self.assertFalse(validate_username("user name"))  # Space not allowed
    
    def test_validate_email(self):
        """Test email validation"""
        # Valid emails
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("user.name@example.com"))
        self.assertTrue(validate_email("user_name@example.co.uk"))
        
        # Invalid emails
        self.assertFalse(validate_email("user@example"))  # No TLD
        self.assertFalse(validate_email("user@.com"))  # No domain
        self.assertFalse(validate_email("user@example."))  # Incomplete TLD
        self.assertFalse(validate_email("userexample.com"))  # No @ symbol
    
    def test_validate_ip_address(self):
        """Test IP address validation"""
        # Valid IP addresses
        self.assertTrue(validate_ip_address("192.168.1.1"))
        self.assertTrue(validate_ip_address("10.0.0.1"))
        self.assertTrue(validate_ip_address("172.16.0.1"))
        self.assertTrue(validate_ip_address("255.255.255.255"))
        
        # Invalid IP addresses
        self.assertFalse(validate_ip_address("192.168.1"))  # Incomplete
        self.assertFalse(validate_ip_address("192.168.1.256"))  # Out of range
        self.assertFalse(validate_ip_address("192.168.1.1.1"))  # Too many octets
        self.assertFalse(validate_ip_address("192.168.1.a"))  # Non-numeric
    
    def test_check_internet_connection(self):
        """Test internet connection check"""
        # This test may fail if there is no internet connection
        # It's more of a functional test than a unit test
        result = check_internet_connection()
        print(f"Internet connection: {'Available' if result else 'Not available'}")
    
    def test_get_system_info(self):
        """Test system information retrieval"""
        system_info = get_system_info()
        self.assertIsNotNone(system_info)
        self.assertIn("os", system_info)
        self.assertIn("os_version", system_info)
        self.assertIn("architecture", system_info)
        self.assertIn("python_version", system_info)
        self.assertIn("hostname", system_info)

class TestSnapchatTool(unittest.TestCase):
    """Test SnapchatTool class"""
    
    def setUp(self):
        """Set up test environment"""
        self.tool = SnapchatTool()
    
    def test_initialization(self):
        """Test initialization"""
        self.assertIsNotNone(self.tool.session)
        self.assertIsNone(self.tool.token)
        self.assertIsNotNone(self.tool.user_agent)
        self.assertIsNotNone(self.tool.headers)
    
    def test_login_simulation(self):
        """Test login simulation"""
        # This is a simulation, so it should always succeed
        result = self.tool.login("test_user", "test_password")
        self.assertTrue(result)
        self.assertIsNotNone(self.tool.token)
    
    def test_get_user_info_simulation(self):
        """Test user info retrieval simulation"""
        # Login first
        self.tool.login("test_user", "test_password")
        
        # Get user info
        user_info = self.tool.get_user_info("target_user")
        self.assertIsNotNone(user_info)
        self.assertEqual(user_info["username"], "target_user")
        self.assertIn("email", user_info)
        self.assertIn("ip_address", user_info)
        self.assertIn("location", user_info)

class TestAdvancedFeatures(unittest.TestCase):
    """Test AdvancedFeatures class"""
    
    def setUp(self):
        """Set up test environment"""
        self.advanced = AdvancedFeatures("test_token")
    
    def test_initialization(self):
        """Test initialization"""
        self.assertIsNotNone(self.advanced.session)
        self.assertEqual(self.advanced.auth_token, "test_token")
        self.assertIsNotNone(self.advanced.headers)
    
    def test_get_ip_info_simulation(self):
        """Test IP info retrieval simulation"""
        ip_info = self.advanced.get_ip_info("192.168.1.1")
        self.assertIsNotNone(ip_info)
        self.assertEqual(ip_info["ip"], "192.168.1.1")
        self.assertIn("country", ip_info)
        self.assertIn("region", ip_info)
        self.assertIn("city", ip_info)
    
    def test_get_account_security_simulation(self):
        """Test account security retrieval simulation"""
        security_info = self.advanced.get_account_security("test_user")
        self.assertIsNotNone(security_info)
        self.assertEqual(security_info["username"], "test_user")
        self.assertIn("two_factor_enabled", security_info)
        self.assertIn("login_verification", security_info)
        self.assertIn("recovery_email", security_info)
    
    def test_get_account_activity_simulation(self):
        """Test account activity retrieval simulation"""
        activity_info = self.advanced.get_account_activity("test_user")
        self.assertIsNotNone(activity_info)
        self.assertEqual(activity_info["username"], "test_user")
        self.assertIn("last_login", activity_info)
        self.assertIn("login_ip", activity_info)
        self.assertIn("recent_locations", activity_info)

if __name__ == "__main__":
    unittest.main()