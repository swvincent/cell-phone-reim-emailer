# cell-reim

Quick &amp; dirty python script that submits my monthly cell phone reimbursement request to my boss. It creates a PDF expense report, attaches it to an email and sends it to a specified email address.

It uses pyfpdf to generate an expense report in PDF format which is then attached to an email and send to my boss. I schedule it with cron.

It relies on pyfpdf's write_html function which I found difficult to use well and very limited. If I ever update this I'll use a different method/software to generate the PDF.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This program requires Python 3 and the following libraries from PyPi: [retrying](https://pypi.org/project/retrying/) and [fpdf2](https://pypi.org/project/fpdf2/)

I had trouble installing fpdf2 on one of my computers. Installing libjpeg-dev using apt install and [pillow](https://pypi.org/project/Pillow/) from PyPi first allowed it to install properly.

### Installing

Install the prerequisite libraries. In cellreim.py, change the server address, from email address and to email address to appropriate values.

## Deployment

Use the cellreim.sh script to schedule the program using cron.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [This example](https://stackoverflow.com/questions/28821487/multipart-email-pdf-attachment-blank/28825053#28825053) by SO user mhawke got me on the right track with building the email message
* [Kenneth Reitz's article on Repository structure](https://www.kennethreitz.org/essays/repository-structure-and-python) helped me figure out where to put everything.
* [PurpleBooth's README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) was used as a reference for creating this README (it's my first!)