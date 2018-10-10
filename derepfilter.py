from Bio import SeqIO
with open("ucout") as uc:
    ucDict = {}
    for line in uc:
        if line.split("\t")[0] == "S":
            hit = line.split("\t")[8]
            ucDict[hit] = [[],[]]
            ucDict[hit][0].append(line.split("\t")[8].split("|")[-1].strip())
            ucDict[hit][1].append(line.split("\t")[8].split("|")[1] + "|" + line.split("\t")[8].split("|")[-1].strip())
        if line.split("\t")[0] == "H":
            ucDict[hit][0].append(line.split("\t")[8].split("|")[-1].strip())
            ucDict[hit][1].append(line.split("\t")[8].split("|")[1]+"|"+line.split("\t")[8].split("|")[-1].strip())

count = 0
ids = []
for duplicate in ucDict:
    ucDict[duplicate][0]
    doubles = list(set(ucDict[duplicate][0]))
    speciesList = []
    if len(doubles) > 1:
        #print ucDict[duplicate][1]
        #print doubles
        for x in ucDict[duplicate][1]:
            if x.split("|")[1] in doubles and x.split("|")[1] not in speciesList:
                speciesList.append(x.split("|")[1])
                ids.append(x.split("|")[0])
        count += 1
    else:
        ids.append(duplicate.split("|")[1])

setIds = set(ids)
with open("RefDB_BOLD.fa", "rU") as handle, open("filtered_waterscan.fa", "a") as output:
    for record in SeqIO.parse(handle, "fasta"):
        accession = record.description.split("|")[1]
        if accession in setIds:
            output.write(">"+str(record.description)+"\n")
            output.write(str(record.seq)+"\n")


#print ids
#print count
#print len(ids)