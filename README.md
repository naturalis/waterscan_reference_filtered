# waterscan reference filtering
## The rules for filtering the waterscan reference data in a fixed order
1.Remove all subgenus annotations, as presented in “()” between genus and species name<br />
2.Trim all entries with “sp.” to genus level<br />
3.~~Remove all genus level entries with 100% DNA match to species level entries<br />~~
4.~~Remove all family and higher level entries with 100% DNA match to species level entries (not applicable for Waterscan RefDB)~~<br />
5.Remove entries with 100% DNA match + 100% name match (redundancy)<br />
6.Cases with multiple names with 100% DNA match can be resolved by LCA tool or name checker<br />

## steps
**Remove all subgenus annotations, as presented in “()” between genus and species name**<br />
**Trim all entries with “sp.” to genus level**<br />
```
sed -r 's/ \(.{0,30}\)//g' RefDB_BOLD.fa | sed -r 's/ sp\.[^|]*//g' > newfile.fa
sed 's/ /_/g' newfile.fa > newfile_nospace.fa
```
**Remove entries with 100% DNA match + 100% name match (redundancy)**<br />
Vsearch is used to find the duplicates<br />
```
sudo vsearch --derep_fulllength newfile_nospace.fa --output dereplicated.fa -uc ucout
```
The python script derepfilter.py is used to retrive accessions and write the sequences to a new fasta file. The paths to the input and output files are hardcoded. The script uses the BioPython package
```
python derepfilter.py
```

# Diatome 18S selection genera
## files used
* 18S.fa (See wiki of galaxy-tool-BLAST private)
* 18S.map (See wiki of galaxy-tool-BLAST private)
* rankedlineage.dmp
* PhytoDiatom.xlsx

## steps
```
mkdir output_genera
```
Extract list of genera from rankedlineage.dmp
```
while read line; do grep -wF "$line" rankedlineage.dmp; done < list_diatome_genera.txt > output_genera/diatome_rankedlineage_genera.dmp
```
Extract taxonids from output_genera/diatome_rankedlineage_genera.dmp 
```
awk -F "\t|\t" '{print $1}' output_genera/diatome_rankedlineage_genera.dmp > output_genera/diatome_taxonids_genera.dmp 
```
create temporary V5 blast database
```
makeblastdb2.8.0 -in 18S.fa -dbtype nucl -taxid_map 18S.map -parse_seqids -blastdb_version 5 -out 18S_V5
```
Extract reads from V5 18S.fa blast database
```
ncbi-blast-2.8.0+/bin/blastdbcmd -db 18S_V5 -taxidlist diatome_taxonids_genera.dmp > diatomeselection_18S_genera.fa
```
create indexed blast database
```
ncbi-blast-2.8.0+/bin/makeblastdb -in diatomeselection_18S_genera.fa -dbtype nucl -taxid_map 18S.map -parse_seqids
```
remove temporary V5 blast database
```
rm 18S_V5.*
```

# Diatome 18S selection orders
## files used
* 18S.fa (See wiki of galaxy-tool-BLAST private)
* 18S.map (See wiki of galaxy-tool-BLAST private)
* rankedlineage.dmp
* PhytoDiatom.xlsx

## steps
```
mkdir output_order
```
Extract list of genera from rankedlineage.dmp
```
while read line; do grep -wF "$line" rankedlineage.dmp; done < list_diatome_orders.txt > output_order/diatome_rankedlineage_order.dmp
```
Extract taxonids from output_genera/diatome_rankedlineage_genera.dmp 
```
awk -F "\t|\t" '{print $1}' output_order/diatome_rankedlineage_order.dmp > output_order/diatome_taxonids_order.dmp 
```
create temporary V5 blast database
```
ncbi-blast-2.8.0+/bin/makeblastdb -in 18S.fa -dbtype nucl -taxid_map 18S.map -parse_seqids -blastdb_version 5 -out 18S_V5
```
Extract reads from V5 18S.fa blast database
```
ncbi-blast-2.8.0+/bin/blastdbcmd -db 18S_V5 -taxidlist diatome_taxonids_order.dmp > diatomeselection_18S_order.fa
```
create indexed blast database
```
ncbi-blast-2.8.0+/bin/makeblastdb -in diatomeselection_18S_order.fa -dbtype nucl -taxid_map 18S.map -parse_seqids
```
remove temporary V5 blast database
```
rm 18S_V5.*
```
