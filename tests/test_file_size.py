import os

from tests.fixtures import file_creator


def test_txt_kb_create_file_with_correct_size(file_creator):
    creator = file_creator('.txt', '1KB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024


def test_txt_mb_create_file_with_correct_size(file_creator):
    creator = file_creator('.txt', '1MB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024


def test_txt_gb_create_file_with_correct_size(file_creator):
    creator = file_creator('.txt', '1GB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024 * 1024


def test_bin_kb_create_file_with_correct_size(file_creator):
    creator = file_creator('.bin', '1KB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024


def test_bin_mb_create_file_with_correct_size(file_creator):
    creator = file_creator('.bin', '1MB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024


def test_bin_gb_create_file_with_correct_size(file_creator):
    creator = file_creator('.bin', '1GB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024 * 1024


def test_zip_kb_create_file_with_correct_size(file_creator):
    creator = file_creator('.zip', '1KB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024


def test_zip_mb_create_file_with_correct_size(file_creator):
    creator = file_creator('.zip', '1MB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024


def test_zip_gb_create_file_with_correct_size(file_creator):
    creator = file_creator('.zip', '1GB')
    file_path = creator.create_file()
    assert os.path.getsize(file_path) == 1024 * 1024 * 1024
