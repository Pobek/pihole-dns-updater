import os
import sys
import subprocess

from flask import jsonify, request 

from config import Config
from app import app, util, cfg

@app.route("/dns", methods=["GET", "PUT", "POST", "DELETE"])
def index():
  cfg.PIHOLE_HOSTS = util.load_hosts(cfg.PIHOLE_HOSTS_FILE)
  
  if request.method == "GET":
    return jsonify({"File": cfg.PIHOLE_HOSTS_FILE, "Content": cfg.PIHOLE_HOSTS}), 200
      
  elif request.method == "POST":
    try:
      req_ip_address = request.json["ip_address"]
      req_domain = request.json["domain"]
      req_hostname = request.json["hostname"]

      cfg.PIHOLE_HOSTS.append({
        "ip_address" : req_ip_address,
        "domain" : req_domain,
        "hostname" : req_hostname,
      })
      util.save_hosts(cfg.PIHOLE_HOSTS_FILE, cfg.PIHOLE_HOSTS)
      subprocess.run(["systemctl", "restart", "pihole-FTL.service"])
    except Exception as ex:
      return jsonify({"Status": "Error", "Exception": str(ex)}), 500

    return jsonify({"Status": "DNS Added"}), 200

  elif request.method == "PUT":
    return jsonify({"Status": "Unimpleneted", "Message": "Method not implemented yet"}), 405

  elif request.method == "DELETE":
    try:

      forced_deletion = False

      if str(request.args.get("forced")).lower() == "true":
        forced_deletion = True
      
      if not forced_deletion:
        req_ip_address = request.json["ip_address"]

      req_domain = request.json["domain"]

      removed_host = {}
      for host in cfg.PIHOLE_HOSTS:
        if host["domain"] == req_domain:
          if forced_deletion:
            removed_host = host
          elif not forced_deletion and host["ip_address"] == req_ip_address:
            removed_host = host
          
          if not removed_host:
            raise Exception("Couldn't find host.")

          cfg.PIHOLE_HOSTS.remove(removed_host)
          util.save_hosts(cfg.PIHOLE_HOSTS_FILE, cfg.PIHOLE_HOSTS)
          subprocess.run(["systemctl", "restart", "pihole-FTL.service"])
          break
      return jsonify({"Status": "DNS Removed", "Host": removed_host}), 200
    except Exception as ex:
      return jsonify({"Status": "Error", "Exception": str(ex)}), 500
