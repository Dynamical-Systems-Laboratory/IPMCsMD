#!/usr/bin/python3

# ------------------------------------------------------------------
#
#   Suite for testing correctness of .data file structure 
#
# ------------------------------------------------------------------

# Conditions for .data file to have a correct structure
#
#   1) Number of atoms is on line 3
#   2) Number of atom types is on line 9
#   3) Section name is preceeded and followed by a '\n'
#   4) Data follows '\n' after section name and ends with 
#       an '\n'
#   5) Data is continuous (no empty or space only lines in between)
#   6) All data lines in a section have the same number of columns
#   7) There are no None or False entries in data entries
#   8) Data is followed by a '\n' and next section name or end of file
#       (i.e. no multiple '\n's)
#   9) There may be no '\n' after data if it's the end of file
#

import sys
py_path = '../../common/'
sys.path.insert(0, py_path)

import extract_data as ed

class FileStructure:
    ''' Class for testing correctness of .data file structure '''
    # Tests for conditions 1-5 and 8-9

    def __init__(self, data_file, section_names):
        ''' Loads and stores the data and section names '''
        
        # data_file - LAMMPS .data file
        # section_names - list or other iterable of names of
        #       sections to check as strings, e.g. ['Masses', 'Atoms']
        
        self.data_file = data_file
        self.section_names = section_names
        
        with open(self.data_file, 'r') as fin:
            self.data = fin.readlines()
        
        # Identify begining section indices 
        # Assumes section name is the first
        # no-space entry in a line
        self.section_ind = {}
        for nln, line in enumerate(self.data):
            line = line.strip().split()
            if line and line[0] in self.section_names:
                self.section_ind[line[0]] = int(nln)

    def check_atoms_pos(self):
        ''' True if number of atoms is on line 3
                and number of atom types on line 9 '''
        
        if 'atoms' in self.data[2] and 'atom types' in self.data[7]:
            return True
        else:
            return False

    def check_section_structure(self):
        ''' True if section and data structure follows 
                expected relative distribution '''

        # Tests conditions 3, 4, 8, and 9
        
        for section in self.section_names:
            # Position of section tag in the data list
            ind_0 = self.section_ind[section]
            
            # Check if preceeded and followed by '\n'
            if not (self.data[ind_0 - 1] == '\n' and self.data[ind_0 + 1] == '\n'):
                return False
            
            # Check if data follows after first '\n'
            # Assumes first column are numbers
            if not self.first_numeric(self.data[ind_0 + 2]):
                return False

            # Check if data continuous and ends with '\n'
            # i.e. if a '\n' is followed by the next section name
            # or newlines signifying end of file
            trimmed = self.data[ind_0 + 2:]
            ind = 0
            for line in trimmed:
                if not self.first_numeric(line):
                    # If not a number, must be a '\n' 
                    # possibly with space combination
                    if not line.isspace():
                        return False
                    else:
                        # If end of file
                        if ind+1 >= len(trimmed):
                            break
                        # If not the end
                        next_line = self.data[ind_0 + 2 + ind + 1]
                        if next_line.isspace():
                            # There can only be one newline at the end of file
                            return False
                        else:
                            # If not a section name
                            if not next_line.strip() in self.section_names:
                                return False
                            # Move on to the next section
                            break
                ind += 1

        return True

        
    def first_numeric(self, line):
        ''' Checks if the first element of a string line is 
                numeric '''
        
        line = line.strip().split()
        if line:
            return line[0].isdigit()
        else:
            return False

class DataStructure:
    ''' Class for testing correctness of data structure in .data file '''
    # Tests for conditions 6 and 7

    def __init__(self, data_file, section_info):
        ''' Loads and stores the data and section names '''
        
        # data_file - LAMMPS .data file
        # section_info - list of iterable pairs of section name and 
        #   number of columns expected in that section 
        #   e.g. [('Atoms', 9), ('Bonds', 6)]
        # Note that tags ( atom tags at the end of each line - # c,f)
        #   also need to be accounted for and they should count as 2
        #   1 - for # and second for c,f

        self.data_file = data_file
        self.section_info = section_info

    def column_number_test(self):
        ''' Check if all lines in data have expected number of columns '''

        for section_name, num_col in self.section_info:

            # Get all data for this section
            with open(self.data_file, 'r') as fin: 
                data = ed.extract_data_section(fin, section_name)
            
            # Compare number of columns
            for line in data:
                line = line.strip().split()
                if not (len(line) == num_col):
                    return False
        
        return True


    def missing_entries_test(self):
        ''' Check if there are any missing data points '''
        # Missing data points are signified by None or False
        # entries

        for section_name, num_col in self.section_info:

            # Get all data for this section
            with open(self.data_file, 'r') as fin: 
                data = ed.extract_data_section(fin, section_name)
            
            # Check for missing values
            for line in data:
                line = line.strip().split()
                if 'None' in line or 'False' in line:
                    return False
        
        return True


# Example demonstrates the usage and also tests the first 
# setup used for simulations
if __name__ == '__main__':

    # LAMMPS .data file
    lmp_data_file = './test_data/nafion.data'

    #
    # .data file structure tests
    #
   
    section_names = ['Masses', 'Atoms', 'Bonds', 'Angles', 'Dihedrals']
    data_struct = FileStructure(lmp_data_file, section_names)

    print(data_struct.check_atoms_pos())
    print(data_struct.check_section_structure())

    #
    # .data structure of underlying data
    #

    # Number of columns in each section in a sequence of section_names
    column_number = [4, 9, 6, 7, 8, 8]
    section_info = [(x, y) for x, y in zip(section_names, column_number)]

    # Testing class
    data_test = DataStructure(lmp_data_file, section_info)

    print(data_test.missing_entries_test())
    print(data_test.column_number_test())
