from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_maven_notifier(Command):
    assert Command("mvn help:help").rc == 0

    # Check Maven Notifier installed
    cmd = Command("find /opt/maven/apache-maven-3.3.9 | grep --color=never %s",
                  "lib/ext/maven-notifier-")
    assert cmd.rc == 0
