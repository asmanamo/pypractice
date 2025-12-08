"""
Problem
-------
Fetch hostname with NETCONF using ncclient.

Concepts Practiced
------------------
- NETCONF manager
- Filter XML
- Extracting RPC reply
"""

from ncclient import manager
import xmltodict

def netconf_get_hostname(host, user, pwd):
    filter_xml = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
      </native>
    </filter>
    """

    with manager.connect(host=host, port=830, username=user,
                         password=pwd, hostkey_verify=False) as m:

        result = m.get(filter_xml).xml
        parsed = xmltodict.parse(result)
        return parsed


if __name__ == "__main__":
    print("NETCONF ready.")

