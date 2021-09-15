import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Source file name")
parser.add_argument("-s", "--size", help="Print size of file in MB", action="store_true")
parser.add_argument("-m", "--mtime", help="Print modification time in format human/min/sec")
parser.add_argument("--rename", help="Destination file name")
parser.add_argument("-ls", help="Print list of all files in directory", action="store_true")

args = parser.parse_args()
if(not args.file):
    print("No file name was provided")
    exit()

if(args.size):
    print("Size of file ", args.file, ": ", os.stat(args.file).st_size/1024/1024, " MB", sep="")

if(args.mtime=="human"):
    mt = os.stat(args.file).st_mtime
    print("Modification time of file ", args.file, ": %d:%02d:%02d" % ((mt//3600) % 24, (mt//60)%60, mt%60), " (UTC+0)", sep="")

if(args.mtime=="min"):
    mt = os.stat(args.file).st_mtime
    print("Modification time of file ", args.file, ": ", mt/60, " minutes", sep="")

if(args.mtime=="sec"):
    mt = os.stat(args.file).st_mtime
    print("Modification time of file ", args.file, ": ", mt, " seconds", sep="")

if(args.rename):
    os.rename(args.file, args.rename)
    print("Renamed to ", args.rename)

if(args.ls):
    print("List of all files in directory:")
    print(os.listdir())
