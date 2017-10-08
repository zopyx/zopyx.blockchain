
import fs
import fs.opener
import hashlib


def hashes_for_fs(url):

    handle, dummy = fs.opener.open(url)
    walker = handle.walk

    result = list()
    for name in walker.files():
        s256 = hashlib.sha256()
        with handle.open(name, 'rb') as fp:
            s256.update(fp.read())
        result.append(dict(
            name=name,
            hash=s256.hexdigest(),
            hash_method='SHA256'))
    return result

if __name__ == '__main__':
    import sys
    import pprint

    pprint.pprint(hashes_for_fs(sys.argv[-1]))


