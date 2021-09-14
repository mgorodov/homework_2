import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Source file name")
parser.add_argument("-s", "--size", help="Print size of file in KB", action="store_true")
parser.add_argument("-r", "--rename", help="Destination file name")
parser.add_argument("-m", "--mtime", help="Print modification time")

args = parser.parse_args()
if(not args.file):
    print("No file name was provided")
    exit()

if(args.size):
    print("Size of file ", args.file, ": ", os.stat(args.file).st_size/1024/1024, " MB", sep="")

if(args.rename):
    os.rename(args.file, args.rename)

if(args.mtime):
    print("Modification time of file ", args.file, ": ", os.stat(args.file).st_mtime, sep="")


