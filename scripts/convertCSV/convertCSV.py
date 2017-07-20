# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:57:03 2017

@author: michael
This script converts my stanchart account statement to YNAB compatible
format

"""

import csv
import pandas as pd
import logging
import string
import random

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
                memo = line[1].strip() + ' ' + ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
    
                self.table.loc[self.ind] = self.account_name,line[0].strip(),"",memo,line[4].strip(),line[3].strip()
                self.ind += 1


    def runImport(self, filename_in,filename_out):
        data = self.read_csv(filename_in)
        self.process_lines(data)
        logging.debug("Head")
        logging.debug(self.table.head())
        self.table.to_csv(filename_out, sep=',')
        
        
ai = AccountImport()
ai.runImport("AccountTransactions.csv","AccountYNAB.csv")