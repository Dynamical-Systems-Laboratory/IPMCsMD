# Equilibration simulations

## Running the equilibration simulations

* If the `in.file` is not yet present in each seed directory, copy the main dir file and
	- Change the seed value so it matches the corresponding `build.emc` seed 
	- Change the data file and parameter file directory appropriately

* Run each seed as:

```bash
mpirun -n Np lmp_mpi -in in.file
```
where `Np` is the number of MPI processes to be used and `in.file` is the name of LAMMPS input file.

A recommended path is to run it on a dedicated Linux server with a `screen` or use a computer cluster and a standard job submission.

## Postprocessing

* Make sure a `post_processing` directory exists in each seed directory
* On MacOs and Linux operating systems, run the `run_python_part.sh` 
	- This will copy and execute all python scripts in the `post_processing` directory in the main directory (i.e. equilibration/sodium_models/)
* On Windows manually copy the python scripts to each seed, uncomment clearly indicated portions of matlab scripts that will automatically run each python script
* Run matlab code
	- Some results need to pieces of code to be run as indicated
	- The scripts here will generate complete set of results used in our research, as related to the equilibration part   
