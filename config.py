import os

class Config(object):
  PIHOLE_HOSTS_FILE = os.environ.get("PIHOLE_HOSTS_FILE") or "/etc/hosts"
  PIHOLE_HOSTS = ""
  