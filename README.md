Ansible Role: Maven Notifier
============================

[![Tests](https://github.com/gantsign/ansible-role-maven-notifier/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-maven-notifier/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.maven--notifier-blue.svg)](https://galaxy.ansible.com/gantsign/maven-notifier)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-maven-notifier/master/LICENSE)

This role installs the
[Maven Notifier](https://github.com/jcgay/maven-notifier)
extension for Maven authored by
[Jean-Christophe Gay](https://github.com/jcgay).

Requirements
------------

* Ansible >= 2.9

* Linux Distribution

    * Debian Family

        * Debian

            * Stretch (9)
            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

    * RedHat Family

        * Rocky Linux

            * 8

        * Fedora

            * 35

    * SUSE Family

        * openSUSE

            * 15.3

    * Note: other versions are likely to work but have not been tested.

* Maven >= 3.1

    * **Warning:** Maven must be installed from a standard `tar.gz` binary
      package; using this role to modify a copy of Maven installed by your
      Linux distributions package management tool (e.g. `apt-get install`) is
      not recommended.

    * **Recommendation:** use the
      [gantsign.maven](https://galaxy.ansible.com/gantsign/maven) role to
      install Maven.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven Notifier version number
maven_notifier_version: '2.1.2'

# Location of the Maven installation to add the Maven Notifier extension to.
maven_notifier_maven_home: '{{ ansible_local.maven.general.home }}'

# Mirror where to dowload Maven Notifier redistributable package from.
maven_notifier_mirror: 'https://repo.maven.apache.org/maven2/fr/jcgay/maven/maven-notifier/{{ maven_notifier_version }}'

# Directory to store files downloaded for Maven Notifier installation
maven_notifier_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported Maven Notifier Versions

The following versions of Maven Notifier are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `2.1.2`
* `2.1.0`
* `1.10.1`
* `1.10.0`
* `1.9.1`

Advanced Configuration
----------------------

The following role variable is dependent on the Maven Notifier version; to use a
Maven Notifier version **not pre-configured by this role** you must configure the
variable below:

```yaml
# SHA256 sum for the redistributable package (i.e. maven-notifier-{{ maven_notifier_version }}-shaded.jar)
maven_notifier_redis_sha256sum: 'ed6fbb0bffc633cf43b4f52d8aae33ac1ce313f7528ca4aecaa75559f8a3bfd5'
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.maven-notifier
      maven_notifier_maven_home: /opt/maven/apache-maven-3.3.9
```

Related Roles
-------------

You may find the following related roles useful:

* [gantsign.java](https://galaxy.ansible.com/gantsign/java) for installing the
  Oracle JDK.

* [gantsign.maven](https://galaxy.ansible.com/gantsign/maven) for installing
  Apache Maven.

* [gantsign.maven-color](https://galaxy.ansible.com/gantsign/maven-color) for
  providing a GUI notification when a build ends.

    * Installs the [Maven Color](https://github.com/jcgay/maven-color)
      extension for Maven authored by
      [Jean-Christophe Gay](https://github.com/jcgay).

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

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

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
