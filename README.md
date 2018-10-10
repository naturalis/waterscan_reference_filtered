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
