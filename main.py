import os
import subprocess
from flask import Flask, jsonify, request

PIHOLE_HOSTS_FILE=os.environ.get("PIHOLE_HOSTS_FILE") or "/etc/hosts"

app = Flask("pihole-proxy")

@app.route("/dns", methods=["GET", "PUT"])
def index():
  if request.method == "GET":
    with open(PIHOLE_HOSTS_FILE, "r") as stream:
      lan_list = stream.read()
      return jsonify({"File": PIHOLE_HOSTS_FILE, "Content": lan_list.split("\n")}), 200
      
  elif request.method == "PUT":
    ip_address = request.json["ip_address"]
    domain = request.json["domain"]
    hostname = request.json["hostname"]

    try:
      with open(PIHOLE_HOSTS_FILE, "a") as stream:
        stream.write(f"{ip_address} {domain} {hostname}\n")

      subprocess.run(["systemctl", "restart", "pihole-FTL.service"])
    except Exception as ex:
      return jsonify({"Status": "Error", "Exception": str(ex)}), 500

    return jsonify({"Status": "DNS Added"}), 200


app.run(host="0.0.0.0", port=9090)
