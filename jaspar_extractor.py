import os
import pandas as pd

df = pd.read_csv("PATH/TO/YOUR/BED_FILE.bed", header=0, sep="\t")

for i, row in df.iterrows():
    # This command is for Linux OS
    command = './bigBedToBed http://hgdownload.soe.ucsc.edu/gbdb/hg38/jaspar/JASPAR2022.bb OUTPUT_FOLDER/JASPAR__%s.bed -chrom=%s -start=%s -end=%s' % (row['id'], row['chr'], row['start'], row['end'])
    print(command)
    os.system(command)

print("Completed !")