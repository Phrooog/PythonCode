# Student Grades Bar Chart

This project was designed to represent data in an aesthetically pleasing graph. The code was written using Python, its modules, and a ```.csv``` file.

## Purpose

The purpose of this project was to gain better understanding on graphing in Python.

## How to Run

*The code was done in Google Collaboratory by permitting the notebook to access Google Drive.*

If you wish to run the code, there are a few steps.
1. Download the ```.csv``` file titled ```StudentGrades.csv``` and upload it into your Google Drive and within a folder.
2. Give Google Drive access to the notebook.
3. Change ```MY_PATH``` corresponding to where the ```.csv``` file is stored in Google Drive at line 5 of the code.

## Expected Output

The expected output of this program is a large graph with labeled axis, a title, a legend, and large yellow bars representing the relationship between var 'names' and 'scores.'

## Troubleshooting

1. If the graph does not show up, check that you are using Google Collaboratory. Some programs do not show graphs.
2. If there is a 'file not found' error, check that ```MY_PATH``` is correct.
  > ```FileNotFoundError: [Errno 2] No such file or directory: '/content/drive/MyDrive/datavis/StudentGades.csv'```
     Notice that the filename is missing the 'r.'
  > Another issue may be the capitalization of the ```.csv``` file affecting the output.
3. If a module is not defined, check if your program requires you to manually install it. Google Collaboratory does it automatically, but software such as Pycharm does not.
