from Bio import Entrez, SeqIO
Entrez.email = "me@example.com"
campy_id = "AL111168.1"

# open an url handle for query
handle = Entrez.efetch(db="nucleotide", id=campy_id, rettype="gb", retmode="text")

# read query result records
record = SeqIO.read(handle, "genbank")
handle.close()

# write sequence to fasta file (so you don't have to request again)
SeqIO.write(record, "campy.fa", "fasta")