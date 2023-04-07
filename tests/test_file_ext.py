import os

from tests.fixtures import file_creator


def test_txt_create_file_with_correct_extension(file_creator):
    creator = file_creator('.txt', None)
    file_path = creator.create_file()
    assert os.path.splitext(file_path)[1] == '.txt'


def test_bin_create_file_with_correct_extension(file_creator):
    creator = file_creator('.bin', None)
    file_path = creator.create_file()
    assert os.path.splitext(file_path)[1] == '.bin'


def test_zip_create_file_with_correct_extension(file_creator):
    creator = file_creator('.zip', None)
    file_path = creator.create_file()
    assert os.path.splitext(file_path)[1] == '.zip'
