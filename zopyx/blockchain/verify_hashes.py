import os
import json
import fs
import fs.opener
import tempfile
import hashlib
import lxml.etree


from zopyx.blockchain.hashes import sha256_for_name

# Dictify hashes from JSON hash file
def hashes_from_json(json_filename):
    hashes = dict()
    with open(json_filename, 'rb') as fp:
        data = json.load(fp)
        for item in data:
            hashes[item['name']] = item['hash']
    return hashes


def verify_hashes(url, hashes, check_all_files=True):

    handle, dummy = fs.opener.open(url)
    walker = handle.walk

    errors = list()
    for name in walker.files():
        hash_calculated = sha256_for_name(handle, name)
        hash_expected = hashes.get(name.lstrip('/'))
        if not hash_expected:
            errors.append('No hash for {name}'.format(name=name))
        if hash_expected and hash_calculated != hash_expected:
            errors.append('Hash for {name} differs'.format(name=name))
        if errors and not check_all_files:
            return errors
    return errors


if __name__ == '__main__':
    import sys
    import pprint
    errors = verify_hashes(
            sys.argv[-2],
            hashes_from_json(sys.argv[-1]))
    pprint.pprint(errors)
