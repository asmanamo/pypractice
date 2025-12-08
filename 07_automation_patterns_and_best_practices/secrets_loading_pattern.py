"""
Problem
-------
Load secrets properly (never hardcode passwords).

Concepts Practiced
------------------
- OS environment
- .env pattern
"""

import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("NMS_USER")
PASSWORD = os.getenv("NMS_PASS")

if __name__ == "__main__":
    print("Secrets loaded:", USERNAME is not None)

