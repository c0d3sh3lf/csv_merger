#!/usr/bin/python

__author__ = "Sumit Shrivastava (@invad3rsam)"
__version__ = "v1.0.0"

###
#   Description:
#   Provide CSV files separated with the commas(,) and the output file
#
#

import optparse

optParse = optparse.OptionParser("csv_merger.py -c <CSV_FILE1>,<CSV_FILE2>,... -o output_file ")
optParse.add_option("-c", "--csv", dest="csvs", help="CSV Files separated by commas")
optParse.add_option("-o", "--output", dest="output_file", help="Output filename")
(options, agrs) = optParse.parse_args()
if (options.csvs != "") and (options.output_file != ""):
    csvs = options.csvs
    csv_list = csvs.split(",")
    counter1 = 1
    for csv in csv_list:
        if counter1==1:
            csv = csv.strip()
            csv_file = open(csv, "r")
            output_file = open(options.output_file, "w")
            for line in csv_file.readlines():
                output_file.write(line)
            csv_file.close()
            output_file.close()
            print "[+] Added", csv, "to", options.output_file
        else:
            counter2 = 1
            csv = csv.strip()
            csv_file = open(csv, "r")
            output_file = open(options.output_file, "a")
            for line in csv_file.readlines():
                if counter2 == 1:
                    pass
                else:
                    output_file.write(line)
                counter2 += 1
            csv_file.close()
            output_file.close()
            print "[+] Added", csv, "to", options.output_file
        counter1 += 1
else:
    print "Please provide CSV(s) and output filename"