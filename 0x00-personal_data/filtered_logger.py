#!/usr/bin/env python3
"""Contains filter_datum function."""
import re

def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """_summary_

    Args:
        fields (list):  strings representing all fields to obfuscate
        redaction (str): string representing by what the field will be obfuscated
        message (str): Log line
        separator (str): Character is separating all fields in the log line (message)

    Returns:
        str: log message obfuscated.
    """
    regex_pattern = f"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(regex_pattern, lambda x: x.group().split('=')[0] + '=' + redaction, message)
