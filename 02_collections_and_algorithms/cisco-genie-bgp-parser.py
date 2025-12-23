"""
Purpose: Parse and filter BGP routes from Cisco Genie (pyATS) output.
Input: Dictionary structure from 'show bgp ipv4 unicast'
"""

# Sample Genie-parsed output for 'show bgp ipv4 unicast'
bgp_data = {
    "bgp": {
        "routes": {
            "10.1.1.0/24": {
                "next_hop": "192.168.0.1",
                "as_path": ["65001", "65002"],
                "origin": "IGP",
                "local_pref": 100,
                "med": 20,
                "community": ["no-export"],
                "best_path": True
            },
            "10.2.2.0/24": {
                "next_hop": "192.168.0.2",
                "as_path": ["65003"],
                "origin": "IGP",
                "local_pref": 200,
                "best_path": True
            }
        }
    }
}

# Simplify access to the routes dictionary
routes = bgp_data["bgp"]["routes"]

print("--- 1. List of All Learned Prefixes ---")
for prefix in routes:
    print(f"Found Prefix: {prefix}")

print("\n--- 2. Next-Hop Lookup (Specific Route) ---")
target = "10.1.1.0/24"
# Use .get() to prevent crashes if the prefix is missing
next_hop = routes.get(target, {}).get("next_hop", "Not Found")
print(f"Next-hop for {target}: {next_hop}")

print("\n--- 3. Filtering: Routes with MED < 50 ---")
for prefix, data in routes.items():
    # Use .get() for MED because not all routes have a MED value
    med_value = data.get("med", 0) 
    if med_value < 50:
        print(f"Match: {prefix} (MED: {med_value})")

print("\n--- 4. Identifying Best Paths ---")
# Creates a list of prefixes where 'best_path' is True
best_paths = [p for p, data in routes.items() if data.get("best_path")]
print(f"Optimized Best Paths: {best_paths}")

print("\n--- 5. AS Path Visualization ---")
for prefix, data in routes.items():
    # Convert the AS Path list into a space-separated string
    as_string = " ".join(data.get("as_path", ["Internal"]))
    print(f"{prefix.ljust(15)} | AS Path: {as_string}")
