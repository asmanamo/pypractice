"""
Problem
-------
Render interface config using Jinja2 template.

Concepts Practiced
------------------
- config templating
- automation-friendly design
"""

from jinja2 import Template

tpl = """
interface {{ intf }}
 description {{ desc }}
 ip address {{ ip }} {{ mask }}
"""

def render(intf, desc, ip, mask):
    template = Template(tpl)
    return template.render(intf=intf, desc=desc, ip=ip, mask=mask)


if __name__ == "__main__":
    print(render("Gi0/1", "Uplink", "10.1.1.1", "255.255.255.0"))

