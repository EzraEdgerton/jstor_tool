JSTOR TOOL:

This is a tool designed to easily filter large jstor sets for specific search terms
and to easily create exploratory web visualizations.

You will need a folder with the jstor data you want to explore, formatted with ngram files and xml files for each article.

TO USE:
FILTER & FORMAT:
To filter the data, run jstor_tool.py with the path to the jstor data as the first argument and the path that you wish to write the data to as the second argument. Check the arguments descriptor in the jstor_tool.py file for additional search and filter options. You can filter by publishers, journals, search terms, authors, year range.

and example run, to create a data.json file for articles in the dataset that contain the words "red", "green", "blue"  between 1990 and 2000 would look like this:

python jstor_tool.py jstordatapath/ writepath/ -ys 1990 -ye 2000 -s "red,green,blue"


That will create a file named data.json in the specified write folder.



VISUALIZE:
To create the html to visualize the data, run jstor_format.py with the first argument as the writepath you specified in the filter&format step. It will prompt you for the type of visualization you want to create and the fields you wish to create it for. Once that is run, the html will be created in the specified writepath folder. 

NOTE ON VISUALIZATION:
Things tend to get incredibly messy and hard to render when specifying fields that have many unique names (i.e. authors, title, path). It is recommended that you do not create a force graph with these fields as it will be incredibly clunky to render. Hopefully updates can remedy this.

TO VIEW:
in this folder, run python -m SimpleHTTPServer and then go to http://0.0.0.0:8000/writepath/ to view the html files you have created.

