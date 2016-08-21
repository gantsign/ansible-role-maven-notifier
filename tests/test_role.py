def test_maven_notifier(Command):
    assert Command("mvn help:help").rc == 0

    # Check Maven Notifier installed
    cmd = Command("find /opt/maven/apache-maven-3.3.9 | grep --color=never 'lib/ext/maven-notifier-'")
    assert cmd.rc == 0
