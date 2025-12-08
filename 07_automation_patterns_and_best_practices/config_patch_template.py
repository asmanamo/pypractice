"""
Problem
-------
Generate minimal patch config from parameters.

Concepts
--------
- Templating for only-changed fields
"""

from jinja2 import Template

patch_template = """
{% if desc %}
description {{ desc }}
{% endif %}
{% if shutdown is not none %}
{% if shutdown %}shutdown{% else %}no shutdown{% endif %}
{% endif %}
"""

def render_patch(desc=None, shutdown=None):
    return Template(patch_template).render(desc=desc, shutdown=shutdown)


if __name__ == "__main__":
    print(render_patch(desc="Uplink", shutdown=False))

