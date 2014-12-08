## Introduction

This directory contains tools for verifying tests.full.xml and converting xml to csv or csv to xml.

## Command
  
To convert tests.full.xml to csv file with command:
    python xml2csv.py -c /path/to/tests.full.xml


To convert csv file to tests.full.xml and tests.xml with command:
    python csv2xml.py -c /path/***.csv


To verify case path, id, purpose and set type are right with command:
    python xmlverifier.py -v /path/***
