"""ENTRY POINT"""

from .app import create_app
import os

os.system("pip install --upgrade pip")

APP = create_app()