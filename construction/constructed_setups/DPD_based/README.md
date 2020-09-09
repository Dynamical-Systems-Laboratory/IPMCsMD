# Construction of Nafion membrane

## EMC part

The membrane is first constructed using the discrete particle dynamics (DPD) functionality of the [EMC software](http://montecarlo.sourceforge.net/emc/Welcome.html). Constructions involves several steps:

1. Change the default DPD parameters

  * The parameters are located in field/dpd/ directory of EMC

  * In `general.prm` change the `MASS` from
```
ITEM    MASS

# type  mass    name    ncons   charge  comment

*   1   *   2   0   anything

ITEM    END

```
    to 

```
ITEM    MASS

# type  mass    name    ncons   charge  comment

*   20.0    *   2   0   anything
 
ITEM    END

```

  * Then uncomment the `ANGLE` parameters so the entry looks like this:

```
ITEM    ANGLE_AUTO

# type1 type2   type3   k   theta0

*   *   *   4.0 180.0

ITEM    END 

``` 

  * Add the dihedral portion

```
# Dihedral wildcard parameters

# type1 type2   type3   k   theta0

*   *   *   * 0 0 0 0

ITEM    END
```

2. Copy the `polymer.sh` template from `construction/parameters/dpd_templates/`
   * This file determines the structure and connectivity of the polymer chain so anything related to it should be changed here
3. Run `/.../scripts/emc_setup.pl polymer.sh`
4. This will create a file `build.emc`. Using `build.emc` from `construction/parameters/dpd_templates/` as a syntax guide:
   * Substitute all the partial charges to their correct values. Right now the full entry is:

```

  chem_ngroup    -> "*[C+0.32750]([F-0.15760])([F-0.15760])[C+0.32750]([F-0.15760])([F-0.15760])*",
  chem_mgroup   -> "*[C+0.2465]([F-0.1336])([F-0.1336])[C+0.1317]([F-0.1193])*[Oc-0.3109][C+0.4954]([F-0.1280])([F-0.1559])[C+0.0465]([F-0.1122])([C+0.5842]([F-0.1563])([F-0.1736])[F-0.1844])[Oc-0.2516][C+0.4557]([F-0.1368])([F-0.1393])[C+0.1062]([F-0.1457])([F-0.1482])[S+1.1345](=[Os-0.6371])(=[Os-0.6371])[Os-0.6371][Na+1.0]",
  chem_tgroup   -> "*[F-0.161]",
  chem_water    -> "[H+0.4238][O-0.8476][H+0.4238]"
  
```
  * Set the random seed. This is not necessary, but throught this work the same random seed was used for creating the system and later for its simulation. One way to generate a valid random seed is by copying the last 6 numbers of the current time since the epoch, obtained by running `date '+%s'` in an OsX or Linux terminal.
  * In the `field` entry add `torsion -> empty`, this will cause dihedral interactions to also be created. The whole part looks like the following:

```
field       = {
  id        -> dpd/general,
  mode      -> dpd,
  name      -> location+field+".prm",
  compress  -> false,
  torsion   -> empty
};
```
  * In the LAMMPS entry specify `units` as `real`:

```
lammps      = {name -> output, mode -> put, forcefield -> dpd,
           units->real, parameters -> true, types -> false, unwrap -> true,
           charges -> true, ewald -> true, cross -> true};
```
5. Run `/.../bin/emc_exe build.emc` (where `emc_exe` is the executable for your operating system)

6. Generated structure can be viewed with [VMD](https://www.ks.uiuc.edu/Research/vmd/) by running `vmd -e dpd.vmd`. All the generated files, including the compressed ones, have to present in the directory where this is ran.

To adjust the amout of water and Nafion, one needs to change `f_poly` and `f_water` values as well as `n_total`, all in the begining of the `build.emc` script. Right now this is done by trial and error since the masses of the components are not the real ones and the system density is very low upon generation. This is because otherwise the system would be too compressed, wich stems from the fact that this procedure doesn't generate the system based on real masses and interaction parameters.

## LAMMPS part

The DPD output needs to be converted to a valid LAMMPS input through the following steps:

1. Copy the `dpd.data` into the final directory where system information should be stored

2. Copy the `dpd_example.py` from `/construction/example_scripts/`, rename, change paths etc.; Then just run - this will move columns in the `dpd.data` so that they are in order expected by LAMMPS. It will also exclude any spurious interactions of the counterion. 

3. Substitute correct masses from `construction/parameters/dpd_templates/dpd.data`. This is example for sodium:

```
Masses

       1   12.01115  # c
       2   18.99840  # f
       3   15.99940  # oc
       4   32.06400  # s
       5   15.99940  # o=
       6    22.990   # na+
       7    1.00797  # hw
       8    15.99940  # o*

```

This step can be done before or after Step 2.

All the correct parameters are in the `construction/parameters/` directory, including the output from [LigParGen](http://zarbi.chem.yale.edu/ligpargen/).  
