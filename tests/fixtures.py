import tempfile
import pytest


@pytest.fixture
def file_creator(tmpdir):
    class FileCreator:
        def __init__(self, ext, size):
            self.ext = ext
            self.size = size
            self.tmpdir = tmpdir

        def create_file(self):
            file_ext = self.ext
            file_size = self.size

            if file_size is not None:
                file_size = 0
                file_size = int(file_size)
                file_unit = 'KB'

                if file_size > 1024:
                    file_size /= 1024
                    file_unit = 'MB'

                if file_size > 1024:
                    file_size /= 1024
                    file_unit = 'GB'

                if file_unit == 'KB':
                    file_size *= 1024
                elif file_unit == 'MB':
                    file_size *= 1024 * 1024
                elif file_unit == 'GB':
                    file_size *= 1024 * 1024 * 1024

            with tempfile.NamedTemporaryFile(suffix=self.ext, dir=self.tmpdir) as f:
                f.write(b'\0' * file_size)

                return f.name

    return FileCreator
