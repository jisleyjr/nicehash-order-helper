"""
NiceHash API Configuration Module

This module provides common configuration and initialization for NiceHash API clients.
It handles environment variable loading and creates both public and private API objects.
"""

import nicehash
import os

# Try to load dotenv if available
try:
    from dotenv import load_dotenv
    # Load environment variables from .env file if it exists
    if os.path.exists('.env'):
        load_dotenv()
except ImportError:
    # dotenv not available, continue without it
    pass

# Production - https://www.nicehash.com
HOST = 'https://api2.nicehash.com'

# Pull out of environment variables
ORGANISATION_ID = os.getenv('ORG_ID')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


def get_public_api():
    """
    Create and return a public API object for NiceHash.
    
    Returns:
        nicehash.public_api: Public API client instance
    """
    return nicehash.public_api(HOST, True)


def get_private_api():
    """
    Create and return a private API object for NiceHash.
    
    Returns:
        nicehash.private_api: Private API client instance
    """
    return nicehash.private_api(HOST, ORGANISATION_ID, API_KEY, API_SECRET, True)


def get_algorithms():
    """
    Get all available algorithms from the NiceHash public API.
    
    Returns:
        dict: Dictionary containing all available algorithms
    """
    public_api = get_public_api()
    return public_api.get_algorithms()


def get_api_clients():
    """
    Convenience function to get both public and private API clients.
    
    Returns:
        tuple: (public_api, private_api) instances
    """
    return get_public_api(), get_private_api()
