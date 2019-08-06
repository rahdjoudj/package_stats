#!/usr/bin/env python3
import operator
import itertools

if __name__ == '__main__':

    thisdict = {}

    f = open("mylist", "r")
    for l in f:
        packages_list = l.split(None, 1)[1]
        for p in packages_list.split(','):
            # print(p)
            try:
                thisdict[p] += 1
            except KeyError:
                thisdict[p] = 1

    sorted_d = dict( sorted(thisdict.items(), key=operator.itemgetter(1),reverse=True))

    x = itertools.islice(sorted_d.items(), 0, 10)
    for key, value in x:
        print("{}: {}".format(key, value))

    # for x in list(sorted_d)[0:10]:
    #     print ("{}: {}".format(x,  sorted_d[x]))
