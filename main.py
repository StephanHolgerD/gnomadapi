import os
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.chrome.options import Options
import time
from GnomadAPI.GnomadAPI import GnomadAPI

#!/usr/bin/env python3
import argparse
import sys
#from importlib import resources
def main():
    parser = argparse.ArgumentParser(description='Quick reference free plotting of bam file')

    #requiredNamed = subparsers.add_argument_group('required arguments')
    parser.add_argument('-c','--chromosome', help='name of chromosome/contig', required=True)
    parser.add_argument('-s','--start' ,help='start of region of interest', required=True)
    parser.add_argument('-e', '--end',help='end of the region of interest', required=True)
    parser.add_argument('-v', '--version',help='end of the region of interest', required=True)


    print(parser)
    c=GnomadAPI

if __name__ == "__main__":
    main()
