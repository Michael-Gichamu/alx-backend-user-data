#!/usr/bin/env python3
"""Contains filter_datum function."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Args:
        fields (list): All fields to obfuscate
        redaction (str): field to be obfuscated
        message (str): Log line
        separator (str): Character is separating all fields in the log line.

    Returns:
        str: log message obfuscated.
    """
    regex_pattern = f"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(regex_pattern, lambda x: x.group().split('=')[0] +
                  '=' + redaction, message)
