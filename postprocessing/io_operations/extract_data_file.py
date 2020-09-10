# ------------------------------------------------------------------
#
#   Tools for extraction of data from .data files
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


