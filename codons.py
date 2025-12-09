def create_codon_dict(file_path):
    # Step 1
    
    file = open(file_path)
    rows = file.readlines()
    file.close()

    # step 2

    dic = {}

    for row in rows:
        cells = row.strip().split('\t')
        codon = cells[0]
        animo_acid = cells[2]
        dic[codon] = animo_acid
    return dic
