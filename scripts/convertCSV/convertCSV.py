#!/usr/bin/env python
"""
ConvertCSV
@author: phoexer

This is a lovely little script that converts my stanchart account statement to 
a YNAB compatible format. 

"""
#%reset -f

import os
import sys
import argparse
import csv
import pandas as pd
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class AccountImport(object):
    account_name = 'Default Name'
    table = pd.DataFrame(columns = ("account","date","payee","memo","outflow","inflow"))
    ind = 1
    def read_csv(self, filepath):
        """Reads a book and returns string"""
        s = []
        with open (filepath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if(len(row) > 0):
                    s.append(row)
        return s
    
    def process_header(self, lst):
        if lst[0] == "Account Name":
            self.account_name = lst[1]
              
    def process_lines(self, lines):
        for line in lines:
            l = len(line)
            if(l == 2):
                self.process_header(line)
            elif (l > 5) and (line[0] != "Date"):
                memo = line[1].strip()
    
                self.table.loc[self.ind] = self.account_name,line[0].strip(),"",memo,line[4].strip(),line[3].strip()
                self.ind += 1


    def runImport(self, filename_in,filename_out):
        data = self.read_csv(filename_in)
        self.process_lines(data)
        logging.debug("Head")
        logging.debug(self.table.head())
        self.table.to_csv(filename_out, sep=',')
        
def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file, CSV from Standchart please.")
    parser.add_argument('outfile', help="Output file, name of output file, if it exists it will be overwritten, you were warned")

    args = parser.parse_args(arguments)
    logging.debug("Lets get this party started.")
    
    logging.debug("Input file:" + args.infile)
    logging.debug("Output file:" + args.outfile)
    
    ai = AccountImport()
    ai.runImport(args.infile, args.outfile)

if __name__ == '__main__':
    main(sys.argv[1:])
    #sys.exit(main(sys.argv[1:]))
    
         