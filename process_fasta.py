""" This python script is used to process fasta format files with many fasta
    sequences in it and put each fasta sequence in separate text file within a
    user defined directory. """


import os

def writeFile(title, descrip, seq):
    fw = open(dirname + title + ".fasta.txt", "wt")
    fw.write(descrip)
    seq = seq + "\n"
    fw.write(seq)
    fw.close()


def extractTitle(titleline):
    descrip = titleline
    title = titleline.strip().split("|")[1]
    return descrip, title


dirname = input("Input the target directory: ")
fastafile = input("Input the location of the fasta file: ")

while True:
    if os.path.exists(dirname):
        if os.listdir(dirname) != []:
            userchoice = input("This is not a empty directory, still write fasta sequences (y/n)? ")
            if userchoice not in ["y", "yes", "Y", "Yes", "YES"]:
                dirname = input("Please input a new target directory: ")
            else:
                break
        else:
            break
    else:
        os.mkdir(dirname)
        break

while True:
    try:
        fr = open(fastafile)
        break
    except FileNotFoundError:
        fastafile = input("No such files or directory, input the right path containing target fasta file: ")

seq = ""

for line in fr.readlines():
    if ">" in line:
        if seq == "":
            descrip, title = extractTitle(line)
        else:
            writeFile(title, descrip, seq)
            descrip, title = extractTitle(line)
            seq = ""
    else:
        seq = seq + line.strip()

writeFile(title, descrip, seq)
fr.close()


