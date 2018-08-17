import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_maven_notifier(host):
    assert host.run("mvn help:help").rc == 0

    # Check Maven Notifier installed
    cmd = "find /opt/maven/apache-maven-3.3.9 | grep --color=never %s"
    assert host.run(cmd, "lib/ext/maven-notifier-").rc == 0
