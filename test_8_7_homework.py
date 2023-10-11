import os
import zipfile
import hashlib


def test_compare_by_hashes():
    files = [
        'Free_Test_Data_300KB_XLSX.xlsx',
        'sample2.txt',
        'test-pdf.pdf',
        'test_Data_XLS.xls'
    ]

    with zipfile.ZipFile('tmp/archive.zip', 'r') as zip_file:
        for file_name in files:
            with open(os.path.join('resources', file_name), 'rb') as f:
                resource_hash = hashlib.md5(f.read()).hexdigest()
            archive_hash = hashlib.md5(zip_file.read(os.path.join('resources', file_name))).hexdigest()
            assert resource_hash == archive_hash

def test_compare_by_content():

    archive_file = 'tmp/archive.zip'
    target_file = 'sample2.txt'
    expected_text = 'restincta siti? Ita relinquet duas'

    with zipfile.ZipFile(archive_file, 'r') as zip_file:
        if target_file in zip_file.namelist():
            zip_file.extract(target_file, 'tmp')
            extracted_file = os.path.join('tmp', target_file)
            with open(extracted_file, 'r') as file:
                file_content = file.read()
            assert expected_text in file_content



def test_compare_by_filenames():
    resource_dir = 'resources'
    archive_file = 'tmp/archive.zip'
    resource_files = [os.path.join(resource_dir, filename) for filename in os.listdir(resource_dir)]
    with zipfile.ZipFile(archive_file, 'r') as zip_file:
        archive_files = zip_file.namelist()

    assert set(resource_files) == set(archive_files)









