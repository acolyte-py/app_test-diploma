import subprocess

from tests.fixtures import file_creator


def test_create_file_with_success_message(file_creator, capsys):
    creator = file_creator('.txt', None)
    file_path = creator.create_file()

    proc = subprocess.Popen(['python', 'file_creator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, _ = proc.communicate(input=f'{file_path}\n'.encode())
    assert 'Успех' in out.decode()

    captured = capsys.readouterr()
    assert 'Файл успешно создан!' in captured.out
