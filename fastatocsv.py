def convert(input,output):
    fasta = open(input, 'r')
    fasta_lines = fasta.readlines()
    seq = {}
    seqs = []

    for line in fasta_lines:

        if line[0] == ">": 
            seqs += [seq] 
            seq_local = {}
            seq_head = line.strip(">\n")
            seq_local["seq_type"] = seq_head 
            seq_local["seq"] = "" 
            seq = seq_local
        else: 
            seq["seq"] += line.strip("\n")
    fasta.close()
    seqs.pop(0) 
    csv_lines = ["Properties, Sequence\n"]
    for seq in seqs:
        csv_line = seq["seq_type"] + "," + seq["seq"] + "\n"
        csv_lines += csv_line
    csv = open(output, 'w')
    csv.writelines(csv_lines)
    csv.close()
    return output


convert("data/moonlight.fasta","data/moonlight.csv")
convert("data/nonMP.fasta","data/nonMP.csv")