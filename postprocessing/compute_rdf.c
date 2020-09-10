#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "math.h"

#define MAXNAME 250
#define MAXL 250
#define MAXW 65
#define LONGS 5000

// Macros
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

// Functions
int parse_string(char* s, char* a[]);
void char_to_float(char* in[], double out[], int nw);
void wrap(double* x, double* y, double* z, double* box[]);
int hist_ind(double i, double j, int num_comp);

/* Program for computing pair (radial) distribution function
 * from a LAMMPS dump file
 * Syntax: compute_pdf <dumpfile> <outputfile>
 * Notes: - Number of atoms assumed fixed
 *        - Box dimensions can vary with each frame
 *        - Currently one output only, output different
 *          than defualt has to be coded at the end of 
 *          the program
 *        - Structure of the file - order and types of 
 *          variables in the dumpfile is hardcoded. To
 *          change, need to modify the program.
 *        - Dump file data part has to start with the
 *          atom ID column, followed by the atom type 
 *          column
 *        - Currently, number of atom types must be < 10  
 *        - Assumes that TIME info is 1st in each frame
 *          and data is the last
 *        - Array sizes above (#define ..) may need to
 *          be made larger based on the input file
 *
 * If not able to locate math library, compile as:
 *
 * 		gcc -O3 -o compute-pdf compute-pdf.c -lm
 *
 * -lm needs to be at the end.
 *	 
*/            

int main(int argc, char *argv[])
{
    // Miscelaneous variables
    char *file_in, *file_out;
    char *sp;
    char s[MAXL],c;
    int i, j, k, flag_frame_0=0, flag_while=1, temp;
    int frame=0, ncl=5, nw=0, show_progress = 500;
    char *wa[MAXW], *boxW[MAXW];
    double w[MAXW], boxTemp[MAXW];
	char *header_name = "ITEM: ATOMS id type x y z\n";
	char *box_header = "ITEM: BOX BOUNDS pp pp pp\n";    

	// Variables for computations
    double x1,y1,z1,dx,dy,dz,dist;
    int time, nat, max_type=0;
    int idst,jdst;

    // Bins
    int kbn, bin, num_bins=300;
    double max_radius=10.0;
    double bin_width=max_radius/num_bins;
    int hist_width;

    // Pointers to files
    FILE *fpi, *fpo;
    
    if(argc!=3){
        printf("Error\n");
        printf("Syntax compute_pdf <dumpfile> <outputfile>\n");
        exit(1);
    }
    // Get the names and open the dump file
    file_in=argv[1];
    file_out=argv[2];
    // 
    fpi=fopen(file_in,"r");
    
    // Preprocessing
    // ---------------------------------------------------------------
    // Read the first frame, find the number of species,
    // first frame time (not needed!), and number of atoms
    while((sp = fgets(s,MAXL,fpi))!= NULL){
        // Collect the timestep
        if(!strcmp(sp,"ITEM: TIMESTEP\n"))
            time = atoi(fgets(s,MAXL,fpi));
        // Collect the atom number
        if(!strcmp(sp,"ITEM: NUMBER OF ATOMS\n"))   
            nat = atoi(fgets(s,MAXL,fpi));
        // Collect the number of types - number of types is the
        // maximum number in the second column of the dump file
        if(!strcmp(sp, header_name)){
            while(strcmp((sp = fgets(s,MAXL,fpi)),"ITEM: TIMESTEP\n")!=0){       
                // Convert sp to array of ints and get the type
                i=0;
                // Moves past numbers from the first column 
                // (atom IDs)
                while(sp[i]!=' '&&sp[i]!='\t')
                    i++;
                // Collects atom type (needs to be < 10)
                temp=sp[++i]-'0';
                // Picks the largest thus far
                max_type=MAX(max_type,temp);  
            }
            // Display number of types
            printf("Number of types: %d\n",max_type);
            break;
        }
    }
    // Back to the begining of the input file
    rewind(fpi);
    
    // Allocate and intialize arrays
    // ---------------------------------------------------------------
    // Array with data from each frame (types, positions, etc.)
    // This one gets overwritten each time
    double** dump_data= (double**) malloc(nat*sizeof(double*));
    for(k=0;k<nat;k++)
        dump_data[k]= (double*) malloc(ncl*sizeof(double));
    // Matrix with box dimensions - also overwritten each time
    double** box= (double**) malloc(3*sizeof(double*));
    for(k=0;k<3;k++)
        box[k]= (double*) malloc(3*sizeof(double));
    // Width of a histogram
    hist_width=1+(max_type*(1+max_type))/2;
    // Matrices with bin data
    int** bin_data= (int**) malloc(num_bins*sizeof(int*));
    for(k=0;k<num_bins;k++)
        bin_data[k]= (int*) malloc(hist_width*sizeof(int));
    for(j=0;j<num_bins;j++)
        for(i=0;i<hist_width;i++)
            bin_data[j][i]=0;
    // Arrays with bin data - computing values here
    double* bin_centers= (double*) malloc(num_bins*sizeof(double));
    for(k=0;k<num_bins;k++)
        bin_centers[k]=(k+0.5)*bin_width;
    double* bin_repvolumes= (double*) malloc(num_bins*sizeof(double));
    for(k=0;k<num_bins;k++)
        bin_repvolumes[k]=1/(((k+1)*(k+1)*(k+1)-k*k*k)*4*bin_width*bin_width*bin_width*M_PI/3);
    
    // Main loop
    // ---------------------------------------------------------------
    while((sp = fgets(s,MAXL,fpi))!= NULL){
        // Box dimensions from dump file
        if(!strcmp(sp, box_header)){
            for(i=0;i<3;i++){
     	        sp = fgets(s,MAXL,fpi);
                nw=parse_string(s,boxW);
                char_to_float(boxW,boxTemp,nw);
                for(j=0;j<2;j++)
                    box[i][j]=boxTemp[j];
            }
    	    // Rearrange/recompute the box
            dx=box[0][1]-box[0][0];
            dy=box[1][1]-box[1][0];
            dz=box[2][1]-box[2][0];
            box[0][0]=dx;
            box[0][1]=0.0;
            box[0][2]=0.0;
            box[1][1]=dy;
            box[1][0]=0.0;
            box[1][2]=0.0;
            box[2][2]=dz;
            box[2][0]=0.0;
            box[2][1]=0.0;
    	}
        // Collect data 
        if(!strcmp(sp, header_name)){
			frame++;
    		i = 0;
            // Get the data as a string, parse it into words and
            // then convert each word to a float saved in dump_data
            // for that frame
            while(i<nat){
    			sp = fgets(s,MAXL,fpi);
               	nw=parse_string(s,wa);
                char_to_float(wa,w,nw);
                for(k=0;k<ncl;k++)
                    dump_data[i][k]=w[k];
                i++;
    		}
            // Compute the distances, wrap them and update (or not)
            // the bin data
            for(idst=0;idst<nat;idst++){
                x1=dump_data[idst][2];
                y1=dump_data[idst][3];
                z1=dump_data[idst][4];
                for(jdst=idst+1;jdst<nat;jdst++){
                    dx=x1-dump_data[jdst][2];
                    dy=y1-dump_data[jdst][3];
                    dz=z1-dump_data[jdst][4];
                    // Wrap 
                    wrap(&dx, &dy, &dz, box);
                    // Compute the distance
                    dist=sqrt(dx*dx+dy*dy+dz*dz);
                    // Bins
                    bin=dist/bin_width;
                    if(bin<num_bins){
                        kbn=hist_ind(dump_data[idst][1],dump_data[jdst][1],max_type);
                        bin_data[bin][0]=bin_data[bin][0]+1;
                        bin_data[bin][kbn]=bin_data[bin][kbn]+1;
                    }                    
                }        
            }
  			// Output progress
			if (frame%show_progress == 0){
				printf("Processing frame number %d\n", frame);
			}
        }
    }               
    
    // Write the results
    // ---------------------------------------------------------------
    // Open the file for writing
    fpo=fopen(file_out,"w");
    // Choose the output
    for(i=0;i<num_bins;i++){
        fprintf(fpo, "%f ", bin_centers[i]);
        for(k=0;k<hist_width;k++){
            // To print the pdf data
            //fprintf(fpo, "%d ", bin_data[i][k]);
            // Or the data that used to be saved by the python script
            fprintf(fpo, "%f ", bin_data[i][k]*bin_repvolumes[i]);    
        }
        fprintf(fpo,"\n");
    }
    // Confirm succesful output
	printf("Program has finished. RDF successfully saved to file.\n");
    
	// Free allocated space
    // ---------------------------------------------------------------
    for(k=0;k<nat;k++)
        free(dump_data[k]);
    free(dump_data);
    for(k=0;k<num_bins;k++){
        free(bin_data[k]);
    }
    free(bin_data);
    free(bin_centers);
    free(bin_repvolumes);
    for(k=0;k<3;k++)
        free(box[k]);
    free(box);
    
    // Close the files
    fclose(fpi);
    fclose(fpo);
}

/* Function to parse a line of input into an aray of words */
/* s - string to be parsed
 * a - string with parsed elements */
int parse_string(char* s,char* a[])
{
    int nw,j; 
    a[0] = strtok(s," \t\n\r\v\f"); 
    nw = 1;				 
    while((a[nw]= strtok(NULL," \t\n\r\v\f"))!=NULL)
        nw++;
   return nw;
}

/* Function to convert array of words to array
 * of doubles
 * in[] - string with pointers to words
 * out[] - string with doubles */ 
void char_to_float(char* in[], double out[], int nw)
{
    int k;
    for(k=0;k<nw;k++)
        out[k]=atof(in[k]);
}

/* Wrap function to preserve periodic boundaries 
 * x, y, z - pointers to x, y and z positions
 * box[] - box dimensions */
void wrap(double* x, double* y, double* z, double* box[])
{
    int i;
    double d2,dxyz, xt=*x, yt=*y, zt=*z, xtt=*x, ytt=*y, ztt=*z;
    for(i=0;i<3;i++){
        d2=0.5*(box[i][0]*box[i][0]+box[i][1]*box[i][1]+box[i][2]*box[i][2]);
        dxyz=box[i][0]*(xtt)+box[i][1]*(ytt)+box[i][2]*(ztt);
        if(dxyz<-d2){
            xt=xt+box[i][0];
            yt=yt+box[i][1];
            zt=zt+box[i][2];
        }else if(dxyz>d2){
            xt=xt-box[i][0];
            yt=yt-box[i][1];
            zt=zt-box[i][2];
        }                                
    }
    *x=xt;
    *y=yt;
    *z=zt;
}

/* Function for mapping from the atom
 * types, i, j to the index in the histogram matrix 
 * num_comp - total number of types */
int hist_ind(double i, double j, int num_comp)
{
    int jj=MIN(i,j);
    int ii=MAX(i,j);
    int ind=(jj-num_comp+ii*(0.5+num_comp)-ii*ii*0.5);
    return ind;
}
 
