import plac
import json


from zopyx.blockchain.verify_hashes import hashes_from_json
from zopyx.blockchain.verify_hashes import verify_hashes


def generate_hashes(url, hashes_json_filename='hashes.json'):

    hashes = hashes_from_json(hashes_json_filename)
    errors = verify_hashes(url, hashes)
    print(errors)


def main():
    plac.call(generate_hashes)
