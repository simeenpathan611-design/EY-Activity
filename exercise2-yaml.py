import yaml
import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(leveltime)s %(message)s")

yaml_content = """
app:
  name:Student Portal
  version:1.0

database:
  host:localhost
  port:3306
  user:root
"""

try:
    config = yaml.safe_load(yaml_content)
    logging.info("config loaded successfully")

    db = config["database"]
    print(f"Connecting to {db['host']}:{db['port']} as {db['user']}")

except yaml.YAMLError as e:
    logging.error(f"YAML parsing error: {e}")
    print(f"Error parsing YAML: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")
    print(f"Unexpected error: {e}")



