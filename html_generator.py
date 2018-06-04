import json
import os
import html_stubs as stubs

def generate_bar_data():

	return -1

def generate_force_data(normal_node, key_node, groups, path):
	f = open(path + "/data.json", "r")
	d = json.load(f)
	returnObj = {"links" : [],
				"nodes" : []}

	keyDict = dict()
	normalDict = dict()
	def add_article(kDict, nDict, a, knode, nnode, subnorm=None, subkey=None):
		if a[knode] in kDict:
			kDict[a[knode]]["count"] += 1
		else:
			kDict[a[knode]] = { "count" : 1,
				"group": 0 }

		if a[nnode] in nDict:
			nDict[a[nnode]]["count"] += 1
		else:
			nDict[a[nnode]] = {
				"count" : 1,
				"group" : 1
			}
		found = False
		for link in returnObj['links']:
			if link['source'] == a[nnode] and link['target'] == a[knode]:
				link['value'] = link['value'] + 1
				found = True
		if not found:
			returnObj["links"].append({
					"source" : a[nnode],
					"target" : a[knode],
					"value" : 1
					})

	for article in d:
		if type(article[key_node]) == list and type(article[normal_node]) == list:
			for subkey in article[key_node]:
				for subnorm in article[normal_node]:

		if type(add_article[normal_node]) and not type(article[key_node]) == list:
			for subnorm in article[normal_node]

		if not type(add_article[normal_node]) and type(article[key_node]) == list:
			for subkey in article[key_node]
		else:
			add_article(keyDict, normalDict, article, key_node, normal_node)
		
	for key in keyDict:
		returnObj["nodes"].append({
			"id" : key,
			"info" : keyDict[key]
			})
	for key in normalDict:
		returnObj["nodes"].append({
			"id" : key,
			"info" : normalDict[key]
			})

	return returnObj

def generate_force_html():
	force_stub_f = open("stubs/force_stub.html", "r")
	force_stub_s = force_stub_f.read()
	force_html_s = force_stub_s


	force_html_f = open("writeplace/force.html", "w")

	force_html_f.write(force_html_s)

	return -1


def generate_bar_html():

	return -1

def generate_bar_files(bars, path):

	finalfile = open(path + "bars.html", "w")

	page = stubs.bar_page_code

	splitpage = page.split("***")

	pagefill = dict()

	pagethingsfill = ["graph_html", "graph_declarations", "dimensions_and_groups", "charts"]


	pagefill["graph_html"] = ""
	pagefill["graph_declarations"] = ""
	pagefill["dimensions_and_groups"] = ""
	pagefill["charts"] = ""
	pagefill["length_calc"] = ""
	for g in bars:
		field = g["x"]
		bartype = g["interaction"]

		if bartype == "linear":
			pagefill["graph_html"] = pagefill["graph_html"] + stubs.bar_html.replace("***field***", field) + "\n"
			pagefill["charts"] = pagefill["charts"] + stubs.bar_linear.replace("***field***", field) + "\n"
		else:
			pagefill["graph_html"] = pagefill["graph_html"] + stubs.bar_long_label_html.replace("***field***", field) + "\n"
			pagefill["charts"] = pagefill["charts"] + stubs.bar_ordinal.replace("***field***", field) + "\n"

		pagefill["graph_declarations"] = pagefill["graph_declarations"] + stubs.jsbardeclare.replace("***field***", field) + "\n"

		pagefill["dimensions_and_groups"] = pagefill["dimensions_and_groups"] + stubs.groupAndDimension.replace("***field***", field) + "\n"


		pagefill["length_calc"] = pagefill["length_calc"] + stubs.length_calc.replace("***field***", field) + "\n"

	for key in pagefill:
		replacekey = "***" + key + "***"
		page = page.replace(replacekey, pagefill[key])


	finalfile.write(page)

	return -1

def generate_force_files(normal_node, key_node, groups, path):


	print "Generating force formatted data..."
	thing = generate_force_data(normal_node, key_node, groups, path)

	writer = open(path + "/force_data.json", "w")
	json.dump(thing, writer, indent=4)
	print "Done"
	#write the file

	generate_force_html()
	return -1