import argparse
import datetime
import os
import pandas as pd
import plot
import sys
import tools

def analyzeStackOverflow(start_date, end_date, input_file, plot_dir):
    print("Analyzing Stack Overflow data...")

    if not os.path.exists(input_file):
        print(f"ERROR: The input file '{input_file}' does not exist.")
        sys.exit(1)

    tools.makeDir(plot_dir)
    
    post_types = ["Questions", "Answers"]

    df = pd.read_csv(input_file, encoding="latin1")

    # Convert date strings to datetime objects
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    
    print("Data frame:")
    print(df)
    print()

    start_date_object, end_date_object = getDateObjects(start_date, end_date)
    plot_name = createPlotName(start_date, end_date)

    print(f" - start date: {start_date}")
    print(f" - end date: {end_date}")
    print(f" - input file: {input_file}")
    print(f" - plot directory: {plot_dir}")
    print(f" - plot name: {plot_name}")

    title = "Stack Overflow Posts"
    x_label = "Time"
    y_label = "Posts per month"
    x_lim = [start_date_object, end_date_object]
    y_lim = [0, 5e5]

    # Use Tableau colors
    colors = {
        "Questions" : "tab:red",
        "Answers"   : "tab:blue"
    }

    plot.makeMultiPlot(df, post_types, plot_dir, plot_name, title, x_label, y_label, x_lim, y_lim, colors)

    print("Done!")

def getDateObjects(start_date, end_date):
    date_format = "%Y-%m-%d"
    start_date_object   = datetime.datetime.strptime(start_date, date_format)
    end_date_object     = datetime.datetime.strptime(end_date, date_format)
    return (start_date_object, end_date_object)

def createPlotName(start_date, end_date):
    start_date_for_name = start_date.replace("-", "_")
    end_date_for_name   = end_date.replace("-", "_")
    plot_name           = "stack_overflow_posts_{0}_to_{1}".format(start_date_for_name, end_date_for_name)
    return plot_name

def main():
    # Arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--start_date", "-a", default="", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date",   "-b", default="", help="End date (YYYY-MM-DD)")
    parser.add_argument("--input_file", "-c", default="", help="Input file (csv)")

    options     = parser.parse_args()
    start_date  = options.start_date
    end_date    = options.end_date
    input_file  = options.input_file

    if not start_date:
        print("Please provide a start date (YYYY-MM-DD) using the -a option.")
        sys.exit(1)

    if not end_date:
        print("Please provide an end date (YYYY-MM-DD) using the -b option.")
        sys.exit(1)
    
    if not input_file:
        print("Please provide an input file (csv) using the -c option.")
        sys.exit(1)
    
    plot_dir    = "stack_overflow_plots"
    analyzeStackOverflow(start_date, end_date, input_file, plot_dir)

if __name__ == "__main__":
    main()
