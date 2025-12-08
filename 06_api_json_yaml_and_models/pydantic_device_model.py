"""
Problem
-------
Create a Pydantic model for device inventory.

Concepts Practiced
------------------
- Data validation
- Type enforcement
"""

from pydantic import BaseModel, IPvAnyAddress, validator

class Device(BaseModel):
    hostname: str
    mgmt_ip: IPvAnyAddress
    os: str
    vendor: str

    @validator("vendor")
    def norm_vendor(cls, v):
        return v.upper()


if __name__ == "__main__":
    d = Device(hostname="r1", mgmt_ip="10.1.1.1", os="xe", vendor="cisco")
    print(d)

