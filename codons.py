def create_codon_dict(file_path):
    # Step 1
    
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()

    # step 2

    codons = {}

    for row in rows:
        components = row.strip().split('\t')
        # row.strip().split('\t')
        codons.update({components[0] : components[1]})
        # codons.update({row[1] : row[3]})
    return codons
