# DataAnalysis

## Plot Stack Overflow Data

The Stack Exchange [Data Explorer](https://data.stackexchange.com/) allows us to collect data from sites in the [Stack Exchange](https://stackexchange.com/) network using SQL queries.
The SQL query [here](https://data.stackexchange.com/stackoverflow/query/1942068/questions-and-answers-per-month) is designed to tabulate the number of questions and answers posted to Stack Overflow per month over a given date range.

1. Choose a working area and clone this repository.
```
git clone https://github.com/caleb-james-smith/DataAnalysis.git
cd DataAnalysis
```

2. Create a Python virtual environment and install the required packages.
```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install numpy pandas matplotlib
```

3. Modify (optional) and run the SQL query [here](https://data.stackexchange.com/stackoverflow/query/1942068/questions-and-answers-per-month).
4. Download the data from the Results tab as a CSV file.
5. Rename (optional) and move the CSV file to your working area.
6. Run the Python script `analyzeStackOverflow.py` to create a plot of the data.

Specify a start date (YYYY-MM-DD), an end date (YYYY-MM-DD), and an input file (.csv)
using the -a, -b, and -c flags, respectively.
```
python python/analyzeStackOverflow.py -a START_DATE -b END_DATE -c INPUT_FILE
```
Here is an example using the start date `2008-01-01`, the end date `2027-01-01`, and the input file `data/StackOverflow_QuestionsAndAnswersPerMonth_v3.csv`.
```
python python/analyzeStackOverflow.py -a 2008-01-01 -b 2027-01-01 -c data/StackOverflow_QuestionsAndAnswersPerMonth_v3.csv
```
The script should save plots in a directory called `stack_overflow_plots`.
