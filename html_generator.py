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
	def add_article(kDict, nDict, a, knode, nnode):
		if knode in kDict:
			kDict[knode]["count"] += 1
		else:
			kDict[knode] = { "count" : 1,
				"group": 0 }

		if nnode in nDict:
			nDict[nnode]["count"] += 1
		else:
			nDict[nnode] = {
				"count" : 1,
				"group" : 1
			}
		found = False
		for link in returnObj['links']:
			if link['source'] == nnode and link['target'] == knode:
				link['value'] = link['value'] + 1
				found = True
		if not found:
			returnObj["links"].append({
					"source" : nnode,
					"target" : knode,
					"value" : 1
					})

	for article in d:

		normal_field = article[normal_node]
		key_field = article[key_node]

		if type(key_field) == list and type(normal_field) == list:
			for subkey in key_field:
				for subnorm in normal_field:
					add_article(keyDict, normalDict, article, subkey, subnorm)

		elif type(normal_field) == list and type(key_field) != list:
			for subnorm in normal_field:
				add_article(keyDict, normalDict, article, key_field, subnorm)

		elif not type(normal_field) != list and type(key_field) == list:
			for subkey in key_field:
				add_article(keyDict, normalDict, article, subkey, normal_field)
		else:
			add_article(keyDict, normalDict, article, key_field, normal_field)
		
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

def generate_force_html(normal_node, key_node, path):
	force_stub_f = open("stubs/force_stub.html", "r")
	force_stub_s = force_stub_f.read()
	force_html_s = force_stub_s.replace("***name***", normal_node + "_" + key_node)


	force_html_f = open(path + normal_node+ "_" + key_node +   "_force.html", "w")

	force_html_f.write(force_html_s)

	return -1


def generate_bar_html():

	return -1

def generate_bar_files(bars, path):

	

	page = stubs.bar_page_code

	pagefill = dict()

	pagethingsfill = ["graph_html", "graph_declarations", "dimensions_and_groups", "charts"]


	pagefill["graph_html"] = ""
	pagefill["graph_declarations"] = ""
	pagefill["dimensions_and_groups"] = ""
	pagefill["charts"] = ""
	pagefill["length_calc"] = ""

	title = ""
	for g in bars:
		field = g["x"]
		title = title + "_" + field
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
	page = page.replace("***name***", title)
	for key in pagefill:
		replacekey = "***" + key + "***"
		page = page.replace(replacekey, pagefill[key])

	finalfile = open(path + title + "_bars.html", "w")
	finalfile.write(page)

	return -1

def generate_force_files(normal_node, key_node, groups, path):


	print "Generating force formatted data..."
	thing = generate_force_data(normal_node, key_node, groups, path)

	writer = open(path + "/" + normal_node + "_" + key_node + "_force_data.json", "w")
	json.dump(thing, writer, indent=4)
	print "Done"
	#write the file

	generate_force_html(normal_node, key_node, path)
	return -1