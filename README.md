Factiva_Sort
============

Python scripts for working with database text files downloaded from Factiva.

/** Running Instructions */
Open terminal and cd to your directory containing factiva_sort.py, ideally you would have your input
files in this directory as well.

Run the command 'python factiva_sort.py [inputs]', [inputs] being any number of text files you would
like to sort. You can also use '*.txt' as the [input] to run all your .txt files into the script.

factiva_sort.py will prompt you to name your output file. Skipping will set the name of the file to 
'output.csv'.



If desired, change format_body to 'True' to have each line of the article bodies separated by a 
newline character. This greatly stretches the .csv file output.

Further changes can be made to 'categories' in the 'Input Specific, Customizable' area. Remove items
in the list that you would not like printed to the output.
*As of now, the neglected categories will be appended onto neighboring ones. Fix coming soon.
