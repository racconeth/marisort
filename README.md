# This is a simple Python code that remove quotation marks and commas from a any .txt EXTENSION this code was inspire by OWASP Maryam

Open-source intelligence(OSINT) uses open-source tools to collect information and analyze them for a specific purpose. OSINT can be very helpful for hackers to use to garner data about particular organizations. Today, using Open sources like bing, google, yahoo, etc, for data gathering, are essential steps for reconnaissance, which is a common task. It should be a tool to automate this routine. One of the best tools in this field is ​The OWASP Maryam.

Installation

The repository can be loaded using the following command:

  git clone https://github.com/racconeth/marisort.git 
  cd marisort
  pip install -r requirements.txt
  pip install getopt


Usage

python code.py -i url.txt -o result.txt

This will run the script, which will open url.txt, read its contents, remove the quotation marks and commas, and write the modified contents to result.txt.
