#!/usr/bin/env python3
"""
Cellphone Reimbursement Request

Written by Scott W. Vincent 9/19/2018.

This is a quick Python program I wrote to automate my cell phone plan
reimbursement requests at work. It was mostly an excuse to get more
Python experience and try out pyfpdf. If I did it again, I would not
use pyfpdf's write_html function to do this. It's very difficult to
generate HTML it "likes" and I had to go with the fpdf2 package as the
original package has a bug that doesn't let font color work. And the
default color was a dark red for some reason. Also elements won't
always center and sizing the logo was tricky.
"""

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from retrying import retry
import logging
from fpdf import FPDF, HTMLMixin        # fpdf2 package, not fpdf!
from datetime import datetime


# Global Constants
MAIL_SERVER = 'somedomain.com'
FROM_EMAIL_ADDRESS = 'employee@somedomain.com'
TO_EMAIL_ADDRESS = 'boss@somedomain.com'

date_string = datetime.today().strftime('%B %Y')


def setup_logger():
    """Setup loggers for file and screen"""
    global logger

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)-12s '
                                  '%(levelname)-8s %(message)s')

    # Log to file
    fh = logging.FileHandler('cellreim.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Log to screen
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info('Program started')


def generate_output_html(htmlfile):
    """Load HTML template and add current date, return result"""
    try:
        with open(htmlfile) as f:
            html = f.read().format(date_string)
            return html
    except Exception as ex:
        logger.error('Exception occured while loading template {}. Details: {}'
                     .format(htmlfile, str(ex)))


@retry(wait_fixed=60000, stop_max_attempt_number=1440)
def send_email(subjectText, msgText, pdf_attachment):
    """
    Send email. Retry every minute until it sends for
    up to 24 hours just to be safe.
    """

    # Very helpful: https://stackoverflow.com/a/28825053
    logger.debug('Attempting to send email "{}"'.format(subjectText))
    attachment = MIMEApplication(pdf_attachment, _subtype="pdf")
    attachment.add_header('content-disposition',
                          'attachment', filename='employee '
                          'expense report {}.pdf'
                          .format(date_string))
    body = MIMEText(msgText)

    msg = MIMEMultipart(_subparts=(body, attachment))
    msg['Subject'] = subjectText
    msg['From'] = FROM_EMAIL_ADDRESS
    msg['To'] = TO_EMAIL_ADDRESS
    msg['Bcc'] = FROM_EMAIL_ADDRESS

    smtp = SMTP(MAIL_SERVER)
    smtp.send_message(msg)
    smtp.quit()


class MyFPDF(FPDF, HTMLMixin):
    pass


# Setup functions
setup_logger()

output_html = generate_output_html('template.html')
logger.debug('Output HTML loaded')

# Create PDF attachment based on generated HTML
pdf = MyFPDF()
pdf.add_page()
pdf.write_html(output_html)

# I had .encode('latin-1') at the end of this line
# but it appears it isn't needed with fpdf2 and it
# causes an error now if I leave it on there.
pdf_attachment = pdf.output(dest='S')
logger.debug('PDF attachment created')

email_subject = 'Cell phone expense report for {}'.format(date_string)
email_body = ('Boss,\n\nPlease see the attached reimbursement request.\n\n'
              'Thanks,\n\nEmployee Name')

try:
    send_email(email_subject, email_body, pdf_attachment)
    logger.info('Email sent')
except Exception as ex:
    # Email failed to send after several retries
    logger.error('Could not send email after several attempts: ' + str(ex))

logger.info('Program finished')
