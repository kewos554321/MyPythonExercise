import math
import sys
import os

def split_jobpair(head, tail, split_number):
    """split a job to job pairs"""
    jobpairs = []
    total_number = tail - head +1
    job_size = total_number // split_number
    residual_job = total_number % split_number
    start = head
    while start <= tail:
        if residual_job:
            stop = start + job_size + 1
        else:
            stop = start + job_size
        if stop > tail:
            jobpairs.append(f"{start}-{tail}")
        else:
            jobpairs.append(f"{start}-{stop}")
        start = stop + 1
    return jobpairs

def make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

class jobfile_generator():

    def __init__(
        self, 
        folder_path="./", 
        save_name="job", 
        script_info="python data/test.py", 
        head=1, 
        tail=123, 
        split_number=12, 
        node_info=[
            (1,60,1), 
            (61,123,2)
            ], 
        module_load=True, 
        qsubjob_reversed=False
        ):

        self.folder_path = folder_path
        self.save_name = save_name
        self.script_info = script_info
        self.head = head
        self.tail = tail
        self.split_number = split_number
        self.node_info = node_info
        self.module_load = module_load
        self.qsubjob_reversed = qsubjob_reversed

    def create_nodelocation_list(self):
        location = [0] * (self.tail-self.head+1)
        for info in self.node_info:
            start, stop, cn = info
            location[start-1:stop] = [cn] * (stop - start + 1)
        return location

    def get_script_info(self, sep='/'):
        lang, info = self.script_info.split(' ')
        info = info.rsplit(sep, 1)
        script_path, script_name = info[0], info[1]
        return (lang, script_path, script_name)

    def create_jobfiles(self):
        make_folder(self.folder_path)
        jobpairs = split_jobpair(self.head, self.tail, self.split_number)
        nodelocation = self.create_nodelocation_list()
        lang, script_path, script_name = self.get_script_info()

        for i, jobpair in enumerate(jobpairs, start=0):
            save_path = f"{self.folder_path}/{self.save_name}_{i+1}.sh"
            cnum = nodelocation[i]
            with open(save_path, "w") as fop:
                fop.write("#!/bin/bash\n")
                if cnum:
                    fop.write(f"#PBS -l nodes=cn{cnum}\n")
                if self.module_load:
                    fop.write(f"module load app/anaconda3/2019.10/x86_64\n")
                fop.write(f"cd {script_path}\n")
                fop.write(f"{lang} {script_name} {jobpair}\n")
        
        self.create_qsubjobfile()

    def create_qsubjobfile(self):
        save_path = f"{self.folder_path}/qsubjob.sh"
        with open(save_path, "w") as fop:
            fop.write(f"#!/bin/bash\n")
            fop.write(f"dos2unix ./*\n")
            if not self.qsubjob_reversed:
                for i in range(self.split_number):
                    fop.write(f"qsub {self.save_name}_{i+1}.sh\n")
            else:
                reversedjob = reversed(range(self.split_number))
                for i in reversedjob:
                    fop.write(f"qsub {self.save_name}_{i+1}.sh\n")
                

if __name__ == "__main__":

    job = jobfile_generator(
        folder_path="./mylabtool/tests/jobfile_generator/data", 
        save_name="job", 
        script_info="python data/test.py", 
        head=19, 
        tail=129, 
        split_number=11, 
        node_info=[
            (1,60,1), 
            (61,123,2)
            ], 
        module_load=True, 
        qsubjob_reversed=True
        )
    job.create_jobfiles()
