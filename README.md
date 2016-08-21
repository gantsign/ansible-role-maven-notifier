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

# Directory to store files downloaded for Maven Notifier installation
maven_notifier_download_dir: "{{ x_ansible_download_dir | default('~/.ansible/tmp/downloads') }}"
```

### Supported Maven Notifier versions

The following versions of Maven Notifier are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `1.9.1`

Advanced Configuration
----------------------

The following role variable is dependent on the Maven Notifier version; to use a
Maven Notifier version **not pre-configured by this role** you must configure the
variable below:

```yaml
# SHA256 sum for the redistributable package (i.e. maven-notifier-{{ maven_notifier_version }}-shaded.jar)
maven_notifier_redis_sha256sum: ed6fbb0bffc633cf43b4f52d8aae33ac1ce313f7528ca4aecaa75559f8a3bfd5
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven-notifier, maven_notifier_maven_home: /opt/maven/apache-maven-3.3.9 }
```

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:
* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
