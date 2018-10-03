import os

SOURCE_DIRS = [
"/Users/johantenbroeke/Sites/projects/fullscreen_3/xcodeprojects/oneonone/Classes/"
]

def scandirs():
	for d in SOURCE_DIRS:
		getFiles(d)

def isSourceCode(filename):
    if ".m" in filename:
        return True
    if ".mm" in filename:
        return True
    return False


def getFiles(dir):
    for f in os.listdir(dir):
        if isSourceCode(f):
            print "** SOURCE FILE **"+f
            sourcefile = open(dir+f)
            lines = sourcefile.readlines()
            for line in lines:
                if "retain" in line:
                    print "\tretain -->"+line
                if "alloc" in line and "dealloc" not in line:
                    print "\talloc -->"+line

            for line in lines:
                if "release" in line:
                    print "\trelease -->"+line

if __name__ == '__main__':
    scandirs()
