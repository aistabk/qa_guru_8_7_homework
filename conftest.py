import pytest
import os
import zipfile
from utils1 import TMP_PATH
import shutil

@pytest.fixture(scope="function", autouse=True)
def test_create_archive():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    with zipfile.ZipFile('tmp/archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        resource_files = os.listdir('resources')

        for file in resource_files:
            zip_file.write(os.path.join('resources', file))


    yield

    shutil.rmtree(TMP_PATH)
