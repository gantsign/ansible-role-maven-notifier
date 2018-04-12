import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_maven_notifier(Command):
    assert Command("mvn help:help").rc == 0

    # Check Maven Notifier installed
    cmd = Command("find /opt/maven/apache-maven-3.3.9 | grep --color=never %s",
                  "lib/ext/maven-notifier-")
    assert cmd.rc == 0
