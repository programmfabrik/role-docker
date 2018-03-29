import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_repo(host):
    assert host.file(
        '/etc/apt/sources.list.d/download_docker_com_linux_{}.list'.format(host.system_info.distribution)
    ).exists


def test_package(Package):
    assert Package('docker-ce').is_installed


def test_service(Service):
    s = Service('docker')

    assert s.is_enabled
    assert s.is_running

def test_docker_hello_world(host):
    assert host.run("docker run -i --rm hello-world").rc == 0
    assert host.run("docker-compose status").rc == 1
