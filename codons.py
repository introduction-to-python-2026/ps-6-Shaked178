def create_codon_dict(file_path):
    # Step 1
    
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()

    # step 2

    codons = {}

    for row in rows:
        row.strip().split('\t')
        codons.update({row[1] : row[3]})
    return codons
