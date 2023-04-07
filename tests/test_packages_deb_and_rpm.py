import pytest

from shutil import which
from subprocess import check_call


def test_install_deb_package():
    if not which('dpkg'):
        pytest.skip('dpkg not found')
    check_call(['sudo', 'dpkg', '-i', '/path/to/*.deb'])
    assert which('*.deb') is not None


def test_install_rpm_package():
    if not which('rpm'):
        pytest.skip('rpm not found')
    check_call(['sudo', 'rpm', '-i', '/home/test/*.rpm'])
    assert which('*.rpm') is not None
