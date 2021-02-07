import csv

def file_to_dict(infile_path: str, outfile_path: str):
    with open(infile_path) as infile, open(outfile_path, "w") as outfile:
        out_writer = csv.writer(outfile, delimiter='\t')
        in_reader = csv.reader(infile, delimiter=':')
        for line in in_reader:
            if line:
                print(line)
                out_writer.writerow((line[0], line[2]))

file_to_dict(infile_path="/etc/passwd", outfile_path="hmm.tsv")
