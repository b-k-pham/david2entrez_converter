## DESCRIPTION
This is a small script created to convert general gene names to ENTREZ ids in the DAVID knowledge base (https://david.ncifcrf.gov/home.jsp). This is useful since one can then upload the converted ids to DAVID directly instead of going through the usual conversion process. The output of this script is a dictionary that takes general gene names as an input and outputs the corresponding ENTREZ id.


# NOTE: I AM NOT AFFILIATED WITH THE DAVID NCIFCRF GROUP. IF FOR ANY REASON USE OF THE DATA IN THIS WAY IS PROHIBITED, PLEASE LET ME KNOW

Anyone can freely retrieve the data themselves following the instructions in this link (https://david-bioinformatics.freeforums.net/thread/42/first-time-user)



## USAGE

First, import the package:

```
from david2entrez_converter import david2entrez_converter
```
Then retrieve the dictionary:

```
z = david2entrez_converter.Gene2Entrez_Dict()
```

Then you can simply plug in your gene names and get the ENTREZ ids out. For example:

```
genes = ['AHI1','NBPF8','NOTCH1']

convert = []

for gene in genes:
    try:
        convert.append(z[gene])
    except:
        pass
        
print(convert)
```

```
[54806, 728841, 4851]
```
