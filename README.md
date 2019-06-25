# Plink2Mega
plink2meg.py converts plink .mdist files to MEGA .meg files. This program took 3 minutes and 40 seconds to convert a plink.mdist with 4700 ids on my computer (8 GB of memory). To view the argments, type the following command in the same directory as plink2meg.py:
```
python3 plink2meg.py --help
```

## Required Input 
plink.mdist and plink.mdist.id files must be found in the same directory as your infile. 
In order to get these files, trim your data however you see fit, and then compute your distance matrix. See the example below:

with a missingness filter of 99% (--geno) and minor allele frequence of 5% (--maf)
```
./plink --file example/example --recode12 --geno .01 --maf .05 --dog --out example/example_miss01maf05
```
and pruning of LD values less than 0.8
```
./plink --file example/example_miss01maf05 --indep-pairwise 50 5 .5 --dog --out example/example_ld08miss01maf05
./plink --file example/example_miss01maf05 --exclude example/example_ld08miss01maf05.prune.out --dog --make-bed --out example/example_ld08miss01maf05
```

Finally, we compute our IBS distance matrix:
```
./plink --bfile example/example_ld08miss01maf05 --autosome --distance 1-ibs --double-id --dog --out example/example_ld08miss01maf05
```

This provides example/example_ld08miss01maf05.mdist and example/example_ld08miss01maf05.mdist.id which are both needed for the plink2meg.py

## Example
Command:
```
python3 plink2meg.py -i example/example_ld08miss01maf05 -o example/example_ld08miss01maf05
```
