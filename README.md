# pihole-remote-dns

This application allows you to add more then one `hostrecord` to PiHole.

The application will create a new file under `dnsmasq.d` that will reference a file filled with `/etc/hosts` style records

Each record under the new file will look like this:

```
<ip-address> <domain> <hostname>

10.0.0.1 master.local.lan master
10.0.0.2 minion1.local.lan minion1
```
