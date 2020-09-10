#!/usr/bin/python3

# ------------------------------------------------------------------
#
#   Tools for extraction of data from various types of files
#
# ------------------------------------------------------------------

def extract_data_section(fin, section_name):
    ''' Collects data from a specific part of a .data file '''
   
    # fin - file handle to avoid the need for absolute paths
    # section_name - name (string) of the part to extract e.g. Masses, Bonds
    # Returns nested list with inner lists being each line of data as a single 
    # string

    # Assumes newline between section name and data and a newline between 
    # data and next section name

    # Find indices bordering the data
    # True if currently iterating through 
    # target section
    found = False
    ind_0 = -1
    ind_f = -1
    data_all = fin.readlines()
    for nln, line in enumerate(data_all):
        if section_name in line:
            # Index where the data begins
            # Accounts for the first newline
            ind_0 = nln + 2
            found = True
        # First condition is to skip the first newline
        if nln > ind_0 and found and line.isspace():
            # Index where the data ends
            ind_f = nln - 1
            found = False
            break

    # Extract and return the data
    # Accounts for the fact that last range element
    # in Python is not included
    return data_all[ind_0:ind_f + 1]

def extract_params_dict(fin, params_name):
    ''' Collects tags and IDs of a given parameter
            type into tag : ID dictionary '''

    # fin - file handle
    # params_name - name of the .params file section; section is
    #   distinguished by the actual coefficient name present in 
    #   each line that defines it e.g. bond_coeff, angle_coeff

    params_dict = {}

    # Due to spaces, the key will be a tuple made out
    # of all atoms in the tag
    for line in fin:
        if params_name in line:
            line = line.strip().split()
            # Find the begining of atom list
            ind = line.index('#') + 1
            # The prepare the tag to be just a list of atoms
            space_tag = ' '.join(line[ind:]).split(',')
            # Remove any extra whitespace
            tag = [x.replace(' ', '') for x in space_tag]

            params_dict[tuple(tag)] = int(line[1])

    return params_dict







