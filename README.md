# waterscan reference filtering
## The set-up rules for filtering the waterscan reference data
1.Remove all subgenus annotations, as presented in “()” between genus and species name<br />
2.Trim all entries with “sp.” to genus level<br />
3.Remove all genus level entries with 100% DNA match to species level entries<br />
4.~~Remove all family and higher level entries with 100% DNA match to species level entries (not applicable for Waterscan RefDB)~~<br />
5.Remove entries with 100% DNA match + 100% name match (redundancy)<br />
6.Cases with multiple names with 100% DNA match can be resolved by LCA tool or name checker<br />
