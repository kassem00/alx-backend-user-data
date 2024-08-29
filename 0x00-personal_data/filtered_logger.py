#!/usr/bin/env python3
"""
This module provides functions for filtering and obfuscating sensitive data 
in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message with a redaction string.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): String to replace field values with.
        message (str): Log message containing fields to obfuscate.
        separator (str): Separator character used to delimit fields in the message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    # Escape the separator for use in the regex pattern
    escaped_separator = re.escape(separator)
    
    # Build the regex pattern
    pattern = rf'({"|".join(fields)})=[^{escaped_separator}]*'
    
    return re.sub(
        pattern,
        lambda m: f'{m.group(1)}={redaction}',
        message
    )
