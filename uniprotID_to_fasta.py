import sys

def OpenFile3Times(file):
    i = 0
    while i <= 1:
        try:
            fr = open(file)
            return fr
            break
        except FileNotFoundError:
            if "fasta" in file:
                file = input("No such file or directory, input right path with fasta file again: ")[1:-1]
            elif "txt" in file:
                file = input("No such file or directory, input right path with protein name file again: ")[1:-1]
            i = i + 1
    return None


def GetFile(file):
    fr = OpenFile3Times(file)
    if fr == None:
        sys.exit()
    return fr


inputfasta = input("Input the path containing the fasta file: ")[1:-1]
inputname = input("Input the file with Uniprot IDs of proteins: ")[1:-1]

ffasta = GetFile(inputfasta)
inputfastalist = ffasta.read().split(">")
ffasta.close()

fname = GetFile(inputname)

selectedfasta = []
for name in fname.readlines():
    name = name.strip()
    for fasta in inputfastalist:
        flag = False
        if name in fasta:
            fasta = ">" + fasta
            selectedfasta.append(fasta)
            flag = True
            break
    if flag == False:
        print("Protein ID <" + name + "> can not match a fasta sequence.")
fname.close()

if "\\" in inputfasta:
    writepath = inputfasta.split("\\")
    writepath = "\\".join([s for s in writepath if s != ""][:-1])
    writepath = writepath + "protein.fasta"

with open(writepath, "wt") as fw:
    for fasta in selectedfasta:
        fw.write(fasta)

    

