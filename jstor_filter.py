import os
import xml.etree.cElementTree as ET
import sys
import string

"""
returns array of objects that correspond to matches with the search terms 
(if specified) in the jstor folder. 
{authors:[]
publisher:[]
date:[year, month]
text: "lorem ipsum dolor et ales bububub"}

CONCERNS: PROBABLY CANT HOLD ALL THAT IN RAM (if text field included)
	solution: probably don't have to. maybe just grab the relevant sentences?
	maybe make it an option? should do test.

THINGS TO DO:
IMPLEMENT MULTILENGTH NGRAMS
IMPLEMENT AND/OR SEARCH
IMPLEMENT MULTIPLE VERSIONS OF AUTHOR NAMES
"""

#no = 0
#totalelementcount = 0
def getMetaFields(xmlfile):
	xmlobj = ET.parse(xmlfile)
	root = xmlobj.getroot()
	year = root.findall('.//year')
	month = root.findall('.//month')
	publisher = root.findall('.//publisher-name')
	journal = root.findall('.//journal-title')
	article_title = root.findall('.//article-title')
	contribs = root.findall('.//contrib')
	art_id = root.findall('.//article-id')
	aff = root.findall('.//aff')

	authors = []

	if len(article_title) == 0:
		article_title = None
	else:
		if article_title[0].text != None:
			article_title = article_title[0].text.lower().strip()
	if len(publisher) == 0:
		publisher = None
	else:
		if publisher[0].text != None:
			publisher = publisher[0].text.lower().strip()
	if len(journal) == 0:
		publisher = None
	else:
		journal = journal[0].text.lower().strip()

	for a in contribs:
		authorstring = ""
		g = a.findall('.//string-name')
		if len(g) != 0:
			i = g[0].itertext()
			for t in i:
				if t.isspace():
					pass
				else:
					authorstring = authorstring + t.lower().strip() + " "
			authors.append(authorstring)

	month_form = month[0].text.translate(None, string.punctuation)
	if len(month_form) > 2:
		month_form = month_form[:2]
	print xmlfile
	return {"year" : int(year[0].text), 
			"month" : int(month_form),
			"pub" : publisher,
			"journal" :  journal, 
			"title" : article_title,
			"authors" :  authors, 
			"path" : xmlfile,
			"words" : []}


def checkAuths(searchthing, meta):
	if len(searchthing) == 0:
		return True
	for s in searchthing:
		for a in meta["authors"]:
			print a.strip()
			print s.lower().strip()
			if s.lower().strip() == a.strip():
				return True
	return False
def checkPubs(searchthing, meta):
	if len(searchthing) == 0:
		return True
	for s in searchthing:
		if meta["pub"] == s.lower().strip():
			return True
	return False
def checkYears(searchthing, meta):
	if meta["year"] >= searchthing[0] and meta["year"] <= searchthing[1]:
			return True
	return False
def checkSearches(searchthing,  path):
	###RIGHT NOW JUST IMPLEMENT ON NGRAMS1 BUT SHOULD  EXTEND
	if len(searchthing) == 0:
		return True
	nmgram1 = open(path, 'r')
	ngrams = nmgram1.read()
	narr = ngrams.split('\n')
	include = False
	words = []
	for x in searchthing:
		for n in narr:
			if x == n.split('\t')[0]:
				words.append(x)
				include = True
	return include, words



def filter(path, authors, publishers, s_terms, dates):
	article_meta = []
	useyear = False
	for root, dirs, files in os.walk(path, topdown=False):
		#If there are not 5 files then formatted incorrectly, skip article
		include = False
		if len(files) != 5:
			pass
		else:
			metadata = {}
			metadata = getMetaFields(os.path.join(root, files[4]))
			authsbool = checkAuths(authors, metadata)
			pubsbool = checkPubs(publishers, metadata)
			yearbool = checkYears(dates, metadata)
			searchbool, metadata["words"] = checkSearches(s_terms, os.path.join(root,files[0]))

			includecheck = [authsbool, pubsbool, yearbool, searchbool]

			include = True
			for b in includecheck:
				if not b:
					include = False
			if include:
				article_meta.append(metadata)
	return article_meta




