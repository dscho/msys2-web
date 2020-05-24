# Copyright 2016-2020 Christoph Reiter
# SPDX-License-Identifier: MIT

import sys
import argparse
from typing import List, Optional, Union

from app import app
from app import appconfig


def main(argv: List[str]) -> Optional[Union[int, str]]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cache", action="store_true",
                        help="use local repo cache")
    parser.add_argument("-p", "--port", type=int, default=8160,
                        help="port number")
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    appconfig.CACHE_LOCAL = args.cache
    print("http://localhost:%d" % args.port)
    app.run(port=args.port, debug=args.debug)

    return None


if __name__ == "__main__":
    sys.exit(main(sys.argv))
