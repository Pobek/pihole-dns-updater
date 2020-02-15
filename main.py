import os
import subprocess
from flask import Flask, jsonify, request

app = Flask("pihole-proxy")


@app.route("/dns", methods=["GET", "PUT"])
def index():
  if request.method == "GET":
    with open("/etc/pihole/lan.list", "r") as stream:
      lan_list = stream.read()
      return jsonify({"File": "/etc/pihole/lan.list", "Content": lan_list.split("\n")}), 200
      
  elif request.method == "PUT":
    ip_address = request.json["ip_address"]
    domain = request.json["domain"]
    hostname = request.json["hostname"]

    try:
      with open("/etc/pihole/lan.list", "a") as stream:
        stream.write(f"{ip_address} {domain} {hostname}\n")

      subprocess.run(["systemctl", "restart", "pihole-FTL.service"])
    except Exception as ex:
      return jsonify({"Status": "Error", "Exception": str(ex)}), 500

    return jsonify({"Status": "DNS Added"}), 200


app.run(host="0.0.0.0", port=9090)
