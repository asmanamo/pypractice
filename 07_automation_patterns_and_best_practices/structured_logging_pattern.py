"""
Problem
-------
Use structured logs instead of print().

Concepts Practiced
------------------
- logging module
- standardized output format
"""

import logging
import json

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_json(**kwargs):
    logger.info(json.dumps(kwargs))


if __name__ == "__main__":
    log_json(event="config_push", device="r1", status="success")

