import os
import json
import fs
import fs.opener
import tempfile
import hashlib
import lxml.etree


def sha256_for_name(fs_handle, name):

    h = hashlib.sha256()

    # normalized XML
    if name.endswith(('.xml', '.XML')):
        with fs_handle.open(name, 'rb') as fp:
            root = lxml.etree.parse(fp)
            tmpf = tempfile.mktemp(suffix='.xml')
            with open(tmpf, 'wb') as fp_out:
                root.write_c14n(fp_out)
            with open(tmpf, 'rb') as fp:
                h.update(fp.read())
            os.unlink(tmpf)
    else:
        with fs_handle.open(name, 'rb') as fp:
            h.update(fp.read())
    return h.hexdigest()


def hashes_for_fs(url):

    handle, dummy = fs.opener.open(url)
    walker = handle.walk

    result = list()
    for name in walker.files():
        h = sha256_for_name(handle, name)
        name = name.lstrip('/')
        result.append(dict(
            name=name,
            hash=h,
            hash_method='SHA256'))
    return result


if __name__ == '__main__':
    import sys
    import pprint
    hashes = hashes_for_fs(sys.argv[-1])
    pprint.pprint(hashes)
    with open('hashes.json', 'w') as fp:
        json.dump(hashes, fp, indent=2)
