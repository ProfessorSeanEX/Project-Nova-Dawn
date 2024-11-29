"""
NovaAI UI Module
-----------------
This package contains all graphical and user interface components for Nova Dawn. 
The primary goal of this package is to provide a seamless, interactive interface 
that visually represents Nova's dynamic state and facilitates user interactions.

Modules Exported:
- GUI Module (gui_static.py): Handles the graphical user interface for NovaAI interactions.
"""

# Import the main GUI launcher from gui_static.py
from .gui_static import launch_gui

# Explicitly defining exports for the UI package
__all__ = [
    "launch_gui",
]
