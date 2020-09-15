# IPMCsMD
Molecular dynamics simulations of ionic polymer metal composites (IPMCs)

## Running the code

To run the code one needs to install [LAMMPS](https://lammps.sandia.gov/).

Anything in this code will run on Linux or MacOS. Windows likely needs adjustments and full functionality is not guaranteed. 

How to run in parallel with MPI

```bash
mpirun -n Np lmp_mpi -in in.file
```

where Np is the number of MPI processes to be used and in.file is the name of LAMMPS input file.

`lmp_mpi` is the LAMMPS exectuable. The path to executable needs to either be full or be added to user's path as

```bash
export PATH=/home/user/lammps/builds/executable:$PATH
```
Path can be anything, elaborated for better demonstration.

List of packages to install with LAMMPS

```
QEQ

MISC

KSPACE

MOLECULE
```

## Directories

Here is a list of directories with their description - detailed descriptions are found in each separate directory and it's README:

* `construction` - directory where the simulation system is constructed from the EMC input. It contains all the parameters and code necessary for construction.
	- `parameters` - all parameters needed for creating the system
	- `example_scripts` - various python templates for system postprocessing and verification
	- `constructed_setups/DPD_based` - main directory with setups that were used in this work
	- `sodium_models`, each `sedd_` directory is one full input to the program, i.e. one system/realization used in this work. In the `seed_` directories the main directory content is the input to the simulations, and the `emc_files` directory is the input to `EMC`. `EMC` is explained in the README but it is not part of this repo, since this would require literal hosting of somebody elses software (`EMC` also invaldidates its binaries upon update thus making its old versions unusable).

* `equilibration/sodium_models/` - this is the directory where all the equilibration is performed, for each seed. As paths are relative, to run, simply execute the above commands on an input in each seed. No other changes necessary. The data used for the publication is located in each seed's directory.

* `simulations` - directory with simulation scripts/results/data. `E1V_nm` and `E5V_nm` are both simulations with the electric field from the paper. The directories contain the code for all the seeds and the results. To re-run, enter each seed directory and run proper `LAMMPS` command with the in.file, nothing else is needed. It also has its own readme explaining the contents.   

* `postprocessing` - this directory contains various postprocessing modules. For description, refer to each modules code, it is documented.

* `tests` - contains all the formal tests developed for this code as well as input verification functionality. Summary:
	- `construction` - the `DPD_tests` are tests for the code that postprocesses the output from `EMC` to make it a suitable input for our model in `LAMMPS`.
	- `input_verification` - scripts used to check if the input for `LAMMPS` is valid   

