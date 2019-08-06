#!/usr/bin/env python3
import operator
import itertools
import urllib.request
import gzip
import sys

class PackageStat(object):

    def __init__(self):
        self.thisdict = {}

    def get_package(self, arch):
        # Download content index
        handle = urllib.request.urlopen('http://ftp.uk.debian.org/debian/dists/stable/main/Contents-' + arch.lower() + '.gz')

        # Store it
        with open('Contents-' + arch.lower() + '.gz', 'wb') as out:
            while True:
                data = handle.read(1024)
                if len(data) == 0: break
                out.write(data)

        # Read it and extract stats
        with gzip.open('Contents-' + arch.lower() + '.gz', 'rb') as f:
            for l in f:
                self.stat_package(l.decode())

    def stat_package(self, l):
        # split each line to gather stats
        packages_list = l.split(None, 1)[1]
        for p in packages_list.split(','):
            # Try to directly increment to win time and not check keys.
            try:
                self.thisdict[p] += 1
            except KeyError:
                self.thisdict[p] = 1

    def stat_result(self):
        # Sort Dictionary by values
        sorted_d = dict( sorted(self.thisdict.items(), key=operator.itemgetter(1),reverse=True))

        # extract the first 10
        x = itertools.islice(sorted_d.items(), 0, 10)
        i = 1 # make it pretty ?
        for key, value in x:
            print("{}. {}: {}".format(i, key.rstrip('\n'), value))
            i += 1


if __name__ == '__main__':

    try:
        arch = sys.argv[1]
    except IndexError:
        print('Please choose your architecture')
        sys.exit(1)

    statme = PackageStat()
    statme.get_package('arm64')
    statme.stat_result()
