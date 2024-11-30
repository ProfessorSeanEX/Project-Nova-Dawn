"""
Core Module Initialization
---------------------------
This file initializes the Core components of NovaAI, making them accessible
as part of the NovaAI/MasterNova/Core package.

Modules Included:
- Library Growth Mechanism (LGM)
- Natural Language Generation (NLG)
- Thoughts Processor
- Voice Generator

Author: CreativeWorkzStudio LLC
"""

# Import modules
from .lgm_library import add_dynamic_knowledge, relate_knowledge, retrieve_dynamic_knowledge
from .nlg_library import generate_response, adjust_tone
from .thoughts_processor import process_thoughts, detect_emotion
from .voice_generator import generate_voice_response

# Define the accessible API
__all__ = [
    "add_dynamic_knowledge",
    "relate_knowledge",
    "retrieve_dynamic_knowledge",
    "generate_response",
    "adjust_tone",
    "process_thoughts",
    "detect_emotion",
    "generate_voice_response",
]
