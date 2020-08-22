# pihole-dns-updater

[![Build Status](https://travis-ci.org/Pobek/pihole-dns-updater.svg?branch=master)](https://travis-ci.org/Pobek/pihole-dns-updater)

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

### Linux

#### Debian/Ubuntu

There is an option to install the application via a `.deb` package.

To do so, download the latest `.deb` package from the releases tab and run:

```bash
sudo dpkg -i <package_name>.deb
```

To run the application, you can call it from the terminal:

```bash
PIHOLE_HOSTS_FILE=/etc/hosts pihole-dns-updater
```

#### Other distros

Coming soon...

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
