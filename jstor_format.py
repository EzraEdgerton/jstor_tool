import argparse
import json
import sys
import html_generator as hg
"""
command line tool for formatting jstor filtered data into efficiently visualizable structures.

Possible vis's:
Bar graph of any of the attributes counts, i.e. count from each publisher or count from each year

Bar graph of each thing by time. Not sure how to group. i.e. a specific publisher over time.
or author over time or word over time

Probably used
Force directed graphs:

"""


parser = argparse.ArgumentParser(description='Format and create html visualization files from jstor data')

parser.add_argument('folderpath', metavar='fp', type=str, nargs=1,
                   help='path where jstor data file exists')

args = parser.parse_args()

def main(_):

	path = args.folderpath[0]

	print("Choose visualization to create:")
	print ("1) Linked graphs")
	print( "2) Force directed graph")
	graph_type = input()

	if graph_type != 1 and graph_type != 2:
		raise Error("Input valid number of option")

	f = open(path + "/data.json", "r")
	data = json.load(f)

	if graph_type == 1:
		moregraphs = True
		graphs_to_build = []
		while moregraphs == True:

			print "Available fields:"
			for d in data[0]:
				print d
			print ""
			print "Select x axis"
			x1 = raw_input()
			print "select domain type (linear/ordinal):"
			interaction= raw_input()

			barg = {"x" : x1,
					"interaction": interaction}

			graphs_to_build.append(barg)

			print "Add another graph? Y/N"
			g = raw_input()

			if g == "N":
				moregraphs = False
			if g == "Y":
				moregraphs = True

		print graphs_to_build	

		hg.generate_bar_files(graphs_to_build, path)
	if graph_type == 2:
		linked_graph = {}
		print "data node field:"

		node_size = raw_input()
		print "key node field:"
		key_node = raw_input()
		print "group field:"
		groups = raw_input()
		hg.generate_force_files(node_size, key_node, groups, path)





main(None)