import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_repo(File):
    assert not File('/etc/apt/sources.list.d/download_docker_com_linux_debian.list').exists
