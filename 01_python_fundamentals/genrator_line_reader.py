def large_file_reader(filepath):
    """Yields one line at a time from a large file."""
    try:
        with open(filepath, 'r') as f:
            for line in f:
                yield line.strip() # Yields the processed line
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")

# Example Usage: Filtering a large log file without memory overhead
log_path = 'server_access.log'
error_count = 0

# The generator only processes the file line-by-line as needed
for record in large_file_reader(log_path):
    if "ERROR" in record:
        error_count += 1
        # Optional: break early if a maximum error count is hit
        
print(f"Total ERROR records found: {error_count}")
