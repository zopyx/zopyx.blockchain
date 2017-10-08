import plac
import json


from zopyx.blockchain.hashes import hashes_for_fs


def generate_hashes(url, hashes_json_filename='hashes.json'):

    hashes = hashes_for_fs(url)
    with open(hashes_json_filename, 'w') as fp:
        json.dump(hashes, fp, indent=2)


def main():
    plac.call(generate_hashes)
