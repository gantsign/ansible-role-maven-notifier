Ansible Role: Maven Notifier
============================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-maven-notifier.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-maven-notifier)

Role to install the Maven Notifier extension for Maven
[https://github.com/jcgay/maven-notifier](https://github.com/jcgay/maven-notifier).

Requirements
------------

Ubuntu with Maven >= 3.1 installed.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven Notifier version number
maven_notifier_version: 1.9.1

# Location of the Maven installation to add the Maven Notifier extension to.
maven_notifier_maven_home: "{{ ansible_local.maven.general.maven_home }}"

# Mirror where to dowload Maven Notifier redistributable package from.
maven_notifier_mirror: "http://dl.bintray.com/jcgay/maven/fr/jcgay/maven/maven-notifier/{{ maven_notifier_version }}"

# SHA256 sum for the redistributable package
maven_notifier_redis_sha256sum: ed6fbb0bffc633cf43b4f52d8aae33ac1ce313f7528ca4aecaa75559f8a3bfd5

# path for Ansible to store downloaded files
local_ansible_data_path: '/tmp/ansible/data'
```

Note: if you install Maven using `groover.maven` role it will set the fact
`ansible_local.maven.general.maven_home`, which this role uses as the default
value for the Maven installation directory. If you install Maven without setting
the fact you will have to specify `maven_notifier_maven_home`.

Example Playbook
----------------

If you install Maven using `groover.maven` this role can be used as follows:

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven_notifier }
```

If you install Maven using a different approach you'll need to specify the
Maven home:

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven_notifier, maven_notifier_maven_home: /opt/maven/apache-maven-3.3.9 }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
