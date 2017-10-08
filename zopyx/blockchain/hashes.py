import os
import fs
import fs.opener
import tempfile
import hashlib
import lxml.etree


def hashes_for_fs(url):

    handle, dummy = fs.opener.open(url)
    walker = handle.walk

    result = list()
    for name in walker.files():

        s256 = hashlib.sha256()

        # normalized XML
        if name.endswith(('.xml', '.XML')):
            with handle.open(name, 'rb') as fp:
                root= lxml.etree.parse(fp)
                tmpf = tempfile.mktemp(suffix='.xml')
                with open(tmpf, 'wb') as fp_out:
                    root.write_c14n(fp_out)
                with open(tmpf, 'rb') as fp:
                    s256.update(fp.read())
                os.unlink(tmpf)
        else:
            # default
            with handle.open(name, 'rb') as fp:
                s256.update(fp.read())

        if name.startswith('/'):
            name = name.lstrip('/')
        result.append(dict(
            name=name,
            hash=s256.hexdigest(),
            hash_method='SHA256'))
    return result

if __name__ == '__main__':
    import sys
    import pprint
    pprint.pprint(hashes_for_fs(sys.argv[-1]))
