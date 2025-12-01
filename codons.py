def create_codon_dict(file_path):
    # Step 1
    file_path = "codons.txt" # "data\codons.txt"

    file = open(file_path, "r")
    rows = file.readlines()
    
    file.close()
