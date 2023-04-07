import os

from tests.fixtures import file_creator


def test_txt_create_file_with_correct_location(file_creator):
    creator = file_creator('.txt', None)
    file_path = creator.create_file()
    assert os.path.dirname(file_path) == str(creator.tmpdir)


def test_bin_create_file_with_correct_location(file_creator):
    creator = file_creator('.bin', None)
    file_path = creator.create_file()
    assert os.path.dirname(file_path) == str(creator.tmpdir)


def test_zip_create_file_with_correct_location(file_creator):
    creator = file_creator('.zip', None)
    file_path = creator.create_file()
    assert os.path.dirname(file_path) == str(creator.tmpdir)
