Ansible Role: Docker
====================

This role installs and configures the bind9 nameserver.

Example play
------------

```yaml
- hosts: all
  vars:
    docker_enabled: yes
  roles:
    blunix.role-docker
```

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
