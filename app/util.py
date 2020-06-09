def load_hosts(path):
  try:
    with open(path, "r") as stream:
      temp_hosts = []

      for line in stream:
        splitted = line.split()
        if len(splitted) > 0:
          file_ip_address = splitted[0]
          file_domain = splitted[1]
          file_hostname = ""
          if len(splitted) > 2:
            file_hostname = splitted[2] 

          temp_hosts.append({
            "ip_address" : file_ip_address,
            "domain" : file_domain,
            "hostname" : file_hostname
          })
    return temp_hosts
  except Exception as ex:
    return []

def save_hosts(path, hosts):
  with open(path, "w") as stream:
    hosts_string = ""
    for host in hosts:
      hosts_string += f'{host["ip_address"]} {host["domain"]} {host["hostname"]}\n'
    
    stream.write(hosts_string)
