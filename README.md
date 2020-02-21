# pihole-remote-dns

This application allows you to add more then one `hostrecord` to PiHole.

The application edits a hosts file with the provided IP-Address, Domain and Hostname.

Each record under the new file will look like this:

```
<ip-address> <domain> <hostname>

10.0.0.1 master.local.lan master
10.0.0.2 minion1.local.lan minion1
```

## Getting Started

Determind which hosts file you would like the application to edit.
This can be either `/etc/hosts` or any other hosts-style like file

### Docker

- Run the following docker command:
  
  ```bash
  docker run -d -p 9090:9090 -e PIHOLE_HOSTS_FILE=/etc/hosts -v /etc/hosts:/etc/hosts pobek/pihole-dns-updater:latest
  ```

- The command will start a docker container which will be exposed on port `9090`.
  The hosts file that will be updated is `/etc/hosts`. A volume must be attached as well so that the container
  can update the `/etc/hosts` file.

### Python

- Install the dependencies from `requirements.yaml`:

  ```bash
  pip3 install -r requirements.txt
  ```

- Run the application. By default it will expose port 9090, and try and edit `/etc/host`.
  This can be changed with the environment variable `PIHOLE_HOSTS_FILE`

  ```bash
  PIHOLE_HOSTS_FILE=/etc/hosts python3 main.py
  ```
