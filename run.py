#!/usr/bin/env python
"""
Run script for the Arbitrage Betting Application.
This script starts the Flask web server.
"""

import os
import sys
from src.app import app

if __name__ == '__main__':
    # Add the current directory to the path so that imports work
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    # Get configuration from environment variables
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Start the Flask application
    app.run(host='0.0.0.0', port=port, debug=debug) 