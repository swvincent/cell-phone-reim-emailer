# cell-reim

Quick &amp; dirty python script that submits my monthly cell phone reimbursement request to my boss. It creates a PDF expense report, attaches it to an email and sends it to a specified email address.

It uses pyfpdf to generate an expense report in PDF format which is then attached to an email and send to my boss. I schedule it with cron.

It relies on pyfpdf's write_html function which I found difficult to use well and very limited. If I ever update this I'll use a different method/software to generate the PDF.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This program requires the following libraries from PyPi: [retrying](https://pypi.org/project/retrying/) and [PyPDF2](https://pypi.org/project/PyPDF2/)

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [This example](https://stackoverflow.com/questions/28821487/multipart-email-pdf-attachment-blank/28825053#28825053) by SO user mhawke got me on the right track with building the email message
* [Kenneth Reitz's article on Repository structure](https://www.kennethreitz.org/essays/repository-structure-and-python) helped me figure out where to put everything.
* [PurpleBooth's README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) was used as a reference for creating this README (it's my first!)