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

	for a in d:
		if a[key_node] in keyDict:
			keyDict[a[key_node]]["count"] += 1
		else:
			keyDict[a[key_node]] = { "count" : 1,
				"group": 0 }

		if a[normal_node] in normalDict:
			normalDict[a[normal_node]]["count"] += 1
		else:
			normalDict[a[normal_node]] = {
				"count" : 1,
				"group" : 1
			}
		found = False
		for link in returnObj['links']:
			if link['source'] == a[normal_node] and link['target'] == a[key_node]:
				link['value'] = link['value'] + 1
				found = True
		if not found:
			returnObj["links"].append({
					"source" : a[normal_node],
					"target" : a[key_node],
					"value" : 1
					})

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
	g = force_stub_s.split("***")

	for x in range(0, len(g) - 1):
		if g[x] == "data":
			g[x] = "forcetestdata.json"
	force_html_s = ""
	for x in g:
		force_html_s = force_html_s + x

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

	thing = generate_force_data(normal_node, key_node, groups, path)

	writer = open(path + "/force_data.json", "w")
	json.dump(thing, writer)
	#write the file

	generate_force_html()
	return -1