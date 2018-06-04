import sys
import xml.etree.cElementTree as ET
import csv
import json
import jstor_filter as jf
import argparse

parser = argparse.ArgumentParser(description='Process jstor folder data for visualization')

parser.add_argument('folderpath', metavar='fp', type=str, nargs=1,
                   help='path where jstor file tree exists')
parser.add_argument('writepath', metavar='wp', type=str, nargs=1,
                   help='path where to write generated data')
parser.add_argument('-ys','--yearstart', metavar='ys', type=int, nargs='?', 
					help="start year for range of jstor articles to be processed")
parser.add_argument('-ye','--yearend', metavar='ye', type=int, nargs='?', 
					help="end year for range of jstor articles to be processed")
parser.add_argument('-af', '--authorfile', metavar='af', type=str, nargs=1, 
					help="path of file with list of authors to include")
parser.add_argument('-pf', '--publisherfile', metavar='af', type=str, nargs=1, 
					help="path of file with list of publishers to include")
parser.add_argument('-sf', '--searchfile', metavar='sf', type=str, nargs=1, 
					help="path of file with list of terms to search article texts and only if include if search result is positive. Will significantly slow process")
parser.add_argument('-a', '--authors', metavar='a', type=str, nargs=1, 
					help="list of authors to filter docs by, separated by commas and no spaces")
parser.add_argument('-p', '--publishers', metavar='a', type=str, nargs=1, 
					help="list of publishers to filter docs by, separated by commas and no spaces")
parser.add_argument('-s', '--searchterms', metavar='s', type=str, nargs=1, 
					help="list of words to search text for and include. will make process run much more slowly, separated by commas and no spaces")

args = parser.parse_args()

def decideSearch(sfile, sterms):
	if sfile != None:
		returnf = open(sfile[0], 'r')
		returns = returnf.read()
		returnterms = returns.split(',')
		return returnterms
	if sterms != None:
		returnterms = sterms[0].split(',')
		return returnterms
	else:
		return []
def decideDate(yearstart, yearend):
	ys = 0
	ye = 4000
	if yearstart is not None:
		ys = yearstart
	if yearend is not None:
		ye = yearend
	return [ys, ye]

#TEST USAGE: jstor_tool.py test/ -s hi,there,my,name,is,test

def main(_):
	print(args)
	path = args.folderpath[0]
	authors = decideSearch(args.authorfile, args.authors)
	publishers = decideSearch(args.publisherfile, args.publishers)
	searchs = decideSearch(args.searchfile, args.searchterms)
	dates = decideDate(args.yearstart, args.yearend)

	articles = jf.filter(path, authors, publishers, searchs, dates)
	for a in articles:
		print a
	#print dates
	writefile = open(args.writepath[0] + "data.json", "w")
	json.dump(articles, writefile, indent=4)

main(None)