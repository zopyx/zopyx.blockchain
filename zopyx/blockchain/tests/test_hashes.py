import os
import fs.opener

from zopyx.blockchain import hashes
from zopyx.blockchain import verify_hashes


data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
fs_url = 'file://' + data_dir
fs_handle, dummy  = fs.opener.open(data_dir)

zip_url = 'zip://' + data_dir + '/../test.zip'


def names2hashes(result):
    name2hash = dict()
    for d in result:
        name2hash[d['name']] = d['hash']
    return name2hash

def test_normalized_xml():
    hash1 = hashes.sha256_for_name(fs_handle, 'test.xml') 
    hash2 = hashes.sha256_for_name(fs_handle, 'test2.xml') 
    assert hash1 == hash2


def test_hashes_for_fs():
    result = hashes.hashes_for_fs(fs_url)
    result_hashes = names2hashes(result)

    assert result_hashes['test.jpg'] == 'a60b193e35133788bce3f8b4ef2b2af1f6e6f1f1438fc6c20033d038938638bc'
    assert result_hashes['test.xml'] == '819d187e76446c6d449a1d7f8cd2c7be48a6f35df96aeb26b656fe80c771ba70'
    assert result_hashes['test2.xml'] == '819d187e76446c6d449a1d7f8cd2c7be48a6f35df96aeb26b656fe80c771ba70'

def test_fs_hashes_zip_hashes():

    fs_result = hashes.hashes_for_fs(fs_url)
    fs_hashes= names2hashes(fs_result)
    errors = verify_hashes.verify_hashes(fs_url, fs_hashes)
    assert len(errors) == 0

    zip_result = hashes.hashes_for_fs(zip_url)
    zip_hashes= names2hashes(zip_result)
    errors = verify_hashes.verify_hashes(zip_url, zip_hashes)
    assert len(errors) == 0

    assert zip_hashes == fs_hashes
