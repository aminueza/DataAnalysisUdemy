import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    key = open(datafile, "r").readline().strip().split(",");
    with open(datafile, "rb") as f:
        dline = f.readline()
        count = 0
        for line in f.readlines():
            if line != dline and count < 10:
                item = line.strip().replace("\t", "").split(",")
                count +=1
                album_dict = {}
                for d, value in enumerate(item):
                    album_dict[key[d].strip()] = value.strip()

                data.append(album_dict)

    return data



def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    print d
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    assert d[0] == firstline
    assert d[9] == tenthline


test()
