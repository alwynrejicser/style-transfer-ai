"""
Content generation and restyling module for Style Transfer AI.
Transforms writing style analysis into creative content generation capabilities.
"""

__version__ = "1.0.0"
__author__ = "Style Transfer AI Team"

from .content_generator import ContentGenerator
from .style_transfer import StyleTransfer
from .templates import GenerationTemplates
from .quality_control import QualityController

__all__ = [
    'ContentGenerator',
    'StyleTransfer', 
    'GenerationTemplates',
    'QualityController'
]