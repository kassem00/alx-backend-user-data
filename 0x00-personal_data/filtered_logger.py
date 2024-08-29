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
    return re.sub(
        rf'({"|".join(fields)})={[^{separator}]*}',
        lambda m: f'{m.group(1)}={redaction}',
        message
    )
