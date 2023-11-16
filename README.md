# Word Count
SysOps Engineer - Take home assessment

*** Assumptions/Instructions ***
1. Assuming this application is to be run in Linux/Mac environment.
2. The application is developed in Python assuming its use for complex tasks as programming languages are more efficient.
3. Shell script can also be used for the same if you want to run a quick analysis. For more complex scenarios, you might prefer a more specialized tool or a programming language.


This command line application uses python or shell script to take .txt file as input and prints a word count of its contents starting with the most frequent word.

There are two ways to run this application : 

1. Using python 

You can run the file 'words_count.py' using command in your terminal: 'python word_count.py path/to/your/file.txt' or 'python3 word_count.py path/to/your/file.txt' depending on your python environment.
It will prompt you for file path input. Replace path/to/your/file.txt with the actual path to the file you want to analyze. The program will then print the word count for each word in the specified file, sorted frequency in descending order.

2. Running shell script 

For that the script has to be executable. Make it uexecutable using 'chmod +x words_count.sh'
You can run the file 'words_count.sh' using command in your terminal: './word_count.sh'. 


