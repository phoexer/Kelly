'''
Created on 3 Oct 2017

@author: michael
This script is something I made for a client as a companion for another project. 
When executed this script scans the src folder and sends an email depending on whether
there are files or not.

'''
import os
import sys
import logging
import configparser
import smtplib
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE

def sendEmail(msg,conf):
    """Sends an email to the addresses set in the config file based on the contents of the src folder."""
    #email Settings
    server = smtplib.SMTP(conf.get('email', 'server-host'), conf.get('email', 'server-post'))
    server.starttls()
    server.login(conf.get('email', 'mail-user'), conf.get('email', 'mail-password'))
    logging.info("Sending Email")
    try:
        server.sendmail(conf.get('email', 'send-from'), send_to, msg.as_string())
        server.quit()
    except:
        logging.error("Unexpected error:", sys.exc_info()[0])
        quit()
    
#Logging stuff
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


conf = configparser.ConfigParser()

logging.info("Starting Kyla")
#logging.error()

conf.read("kyla.cnf")

logging.info("Sections: " + str(conf.sections()))

#get directories
src_dir = conf.get('main', 'source-dir')
bak_dir = conf.get('main', 'backup-dir')


logging.info("Source Directory:\t" + src_dir)
src_files = []


for folder, subs, files in os.walk(src_dir):
    for filename in files:
        src_files.append(os.path.abspath(os.path.join(folder, filename)))

logging.info("List: \t" + str(src_files))


#COMMASPACE = ', '

send_to = conf.get('email', 'send-to').split(',')

msg = MIMEMultipart()

if(len(src_files) == 0 and conf.get('main', 'send-no-files-message')):
    #sending file not found
    logging.info("sending file not found")
    msg['Subject'] = conf.get('email', 'files_not_found_subject')
    msg['From'] = conf.get('email', 'send-from')
    msg['To'] = COMMASPACE.join(send_to)
    #msg.preamble = 'Test email'
    
    with open('files_not_found.html', 'r') as htmlFile:
        files_not_found = htmlFile.read()
        
    msg.attach(MIMEText(files_not_found, 'html'))
    
    sendEmail(msg,conf)
elif(len(src_files) > 0):
    #sending file found
    logging.info("sending file found")
    msg['Subject'] = conf.get('email', 'files_found_subject')
    msg['From'] = conf.get('email', 'send-from')
    msg['To'] = COMMASPACE.join(send_to)
    #msg.preamble = 'Test email'
    
    with open('files_found.html', 'r') as htmlFile:
        files_found = htmlFile.read()
    
    msg.attach(MIMEText(files_found, 'html'))
    
    for src_file in src_files:
        logging.info("Attaching: " + src_file)
        with open(src_file, "rb") as open_file:
            attachment = MIMEApplication(
                open_file.read(),
                Name = os.path.basename(src_file)
            )
        # After the file is closed
        attachment['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(src_file)
        logging.info("Attaching: " + str(attachment))
        msg.attach(attachment)
        
    #Finally send email
    sendEmail(msg,conf)
    
    logging.info("Moving processed files to back up")
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S_') 
    for src_file in src_files:
        os.rename(src_file, os.path.abspath(os.path.join(bak_dir, timestamp + os.path.basename(src_file))))

logging.info("And we're done.")
