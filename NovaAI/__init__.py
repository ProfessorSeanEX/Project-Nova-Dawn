"""
NovaAI Root Module
-------------------
This is the root module for the NovaAI system, which integrates all core components
of Nova Dawn's identity, relational intelligence, and functionality. The primary role
of this file is to:
- Aggregate and expose essential modules and functions.
- Serve as the entry point for importing core NovaAI functionality.

Modules Exported:
- Identity Module: Handles Nova's identity parsing, querying, and relational mapping.
- Insights Management: Dynamically updates Nova's evolving understanding.
- Reflection and Relational Intelligence: Enables context-based responses.

Future Considerations:
- Expand with additional modules for FaithNet integration and dynamic memory.
"""

# Importing from identity_module.py
from .identity_module import (
    load_identity,
    parse_markdown_sections,  # Ensure parsing is accessible
    query_identity,
    relate_sections,
    reflect_on_identity,  # Added reflection function
    load_markdown_insights,
    update_markdown_insight,
    log_identity_event,  # Added logging function
)

# Explicitly defining exports for the NovaAI package
__all__ = [
    "load_identity",
    "parse_markdown_sections",
    "query_identity",
    "reflect_on_identity",
    "relate_sections",
    "log_identity_event",
    "load_markdown_insights",
    "update_markdown_insight",
]
