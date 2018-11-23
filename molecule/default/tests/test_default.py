import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

DOCKER_VERSION = '18.03.0'


def test_apt_repo(host):
    assert host.file(
        '/etc/apt/sources.list.d/download_docker_com_linux_{}.list'.format(
            host.system_info.distribution)
    ).exists


def test_package(host):
    assert host.package('docker-ce').is_installed


def test_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_hello_world(host):
    assert host.run("docker run -i --rm hello-world").rc == 0


def test_docker_compose(host):
    assert not host.file("/usr/bin/docker-compose").exists


def test_version_pinning(host):
    f = host.file('/etc/apt/preferences.d/docker')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0644

    assert f.contains("Pin: version {}*".format(DOCKER_VERSION))
