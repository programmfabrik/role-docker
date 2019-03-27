# Ansible Role: Docker

This role installs and configures Docker and Docker-Compose.

Please note that you have to reboot your machine after installation for docker systemd service to start correctly.
This is because docker needs some kernel modules (error in logs below).
```
gitlab-runner.example.com dockerd[1234]: level=warning msg="Your kernel does not support cgroup rt runtime"
```

# Example play

```yaml
- hosts: all
  vars:
    docker_enabled: yes
    docker_compose_version: 1.14.0

  roles:
    blunix.role-docker
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
