# Stable-matching
Assign students to tasks according to constraints, so as to maximise score.

INSTALLATION

Step 1: Install Python 2.x if you don't have it. https://www.python.org/downloads/

Step 2: Install networkx package (used for network optimisation algorithms). https://pypi.python.org/pypi/networkx/
To install (on Windows), uncompress the folder and launch a terminal. Navigate to the folder containing setup.py, then type the command: "python setup.py install".

Step 3: Download stablematching.py and data.txt to a folder.

USAGE

If you run stablematching.py, it will read the data in data.txt (i.e. the preferences of students) and calculate the best assignment. This assignment will be written to a new file "output.txt" which you can read the answer from.

The key thing is to decide on a scoring system. You assign a certain number of points to each student who manages to secure his first/second/third option, etc. Different scores could lead to different prioritisations. For example you could give 20 points for 1st, 15 for 2nd, and 13 for third. And this would make sure not many people are left without one of their top three choices.

You enter all the details into "data.txt" following a certain format. 

DATA FORMAT

First line: According to your situation, each company must be assigned to by between a and b students, inclusive. Your choice of variables a and b must be entered on the first line, separated by spaces.

Second line: Type your scores for 1st, 2nd, 3rd, etc.

Third line: Type the name of each student, separated by spaces. Each name must be one word only, which can include underscores if you want, e.g. john_doe 

Fourth line: Type the name of each company, separated by spaces. As before, each name must be one word only.

Each remaining line: You type a student's name, leave a space, then hyphen (-), leave another space, then list that student's preferences starting with the first choice. The choices must be separated by spaces.

e.g: john_doe - kfc pizzahut mcdonalds


