''' 
Script for running resolved analysis on the batch
Expects input filelist of files to run on 
One output file produced per input file to chosen output dir
''' 

import os

### User inputs

FILE_LIST = "filelists/TestList.txt"
OUT_DIR = os.getcwd()+"/outputs/test"
USE_BATCH = True

### End of user inputs

# Make output directory 
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)
    os.makedirs(OUT_DIR+"/logs")

# open filelist and read line by line
with open(FILE_LIST, 'r') as filehandle:  
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        file_path = line[:-1]
        # skip if commented out with hash
        if '#' in line: continue
        output_dir = OUT_DIR
        output_filename = file_path.split("/")[-1] # output name same as input name 
        command =  "./build/resolved-recon {0} {1} {2}".format(file_path, output_dir, output_filename)

        if USE_BATCH:
            batch_script = os.getcwd()+"/batchTemplate.sh"
            logfile = OUT_DIR+"/logs/"+output_filename.split(".root")[0]
            batch_command  = "qsub -N {0} -o {1} -e {2} -v CODEDIR='{3}',CMD='{4}' {5}".format(output_filename.split(".root")[0],logfile+".out",logfile+".err",os.getcwd(), command, batch_script)
            print(batch_command)
            os.system(batch_command)
        else: 
          print(command)
          os.system(command)
           
