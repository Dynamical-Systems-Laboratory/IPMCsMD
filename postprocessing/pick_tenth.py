import sys
import random
import collections
from argparse import ArgumentParser  # 2.7+

def parse_cmdline():
    parser = ArgumentParser(description='Sample and save a fraction (1/10) of all snapshots in the input file')
    parser.add_argument("-f", "--file", dest = "fname", required=True,
            help="Input file with snapshots to sample from")
    parser.add_argument("-n", "--number", dest = "SECTIONS_TOTAL",
            help="How many snapshots there are in the input file")
    parser.add_argument("-o", "--out-file", dest = "outfile", 
            help="Output file name, for sampled snapshots")
    parser.add_argument("-m", "--method", dest = "method", default = "random",
            help="How to collect the sample: the first 1/10 or random ones")
    return parser.parse_args()
    #return args


def process_file_pick_first(fname):
    section_no = 0
    with open(fname) as fp, open(outfile, 'w') as out:
        for line in fp:
            if SEC_START in line:
                if section_no >= SEC_NUM:
                    print("Assembled " + str(SEC_NUM) + " sections in the file, " + str(outfile) + ", done")
                    return section_no
                section_no += 1
            if section_no > 0:
                out.write(line)

def process_file_pick_random(fname):
    # Generate a uniform random list of section numbers to take (no dupes though)
    pick_list = sorted( random.sample( range(1,SEC_TOT+1), int(SEC_NUM)) )
    print("Sections to get: ", pick_list)
    # Use deque for speed and convenience
    picks = collections.deque(pick_list)

    section_no = 0         # current section number
    sections_taken = 0     # how many we took so far
    take_section = False   # is the current section on the pick-list?

    with open(fname) as fp, open(outfile, 'w') as out:
        for line in fp:
            if SEC_START in line:
                if sections_taken >= SEC_NUM:
                    print("Assembled " + str(SEC_NUM) + " sections in the file, " + str(outfile) + ", done")
                    return sections_taken
                section_no += 1
                if picks[0] == section_no:
                    take_section = True
                    sections_taken += 1
                    picks.popleft()      # getting this one, remove from list
                    #print("\t==> Taking section number " + str(section_no))
                else:
                    take_section = False
            if take_section:
                out.write(line)
    return sections_taken

SEC_TOT = 0   # total number of "sections" (snapshots) in the file
SEC_NUM = 1   # number to extract, to be set (to an even number close to 1/10 of SEC_TOT)
SEC_START = "ITEM: TIMESTEP"

# === Gather input from command-line
args = parse_cmdline()

# Input filename
if args.fname: fname = args.fname

# Output filename
if args.outfile:
    outfile = args.outfile
else:
    outfile = 'reduced_' + fname

# Total number of sections ("snapshots") in the input file
if args.SECTIONS_TOTAL:
    SEC_TOT = int( args.SECTIONS_TOTAL )
else:
    # Read the file to count the number of section headings
    with open(fname) as fp:
        for line in fp:
            if SEC_START in line: SEC_TOT += 1

# Take first SEC_NUM sections, or random ones? ("random"/"first")
if args.method: method = args.method


# === How many sections ("snapshots") to take
SEC_NUM = SEC_TOT / 10
if (SEC_NUM % 2 != 0):
    SEC_NUM -= 1
print("Split " + str(SEC_NUM) + " sections out of total " + str(SEC_TOT) + " into file " + outfile)

# do it
#
if method == 'random':
    copied_sections = process_file_pick_random(fname);
else:
    copied_sections = process_file_pick_first(fname);

print("Done; copied " + str(copied_sections) + " sections into file " + outfile)

