import argparse
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

    df = pd.read_csv(input_file, encoding="latin1")

    print(df)

    tools.makeDir(plot_dir)

    plot_name = "stack_overflow_posts"

    title = "Stack Overflow Posts"
    x_label = "Time"
    y_label = "Number of posts"
    x_lim = []
    y_lim = []

    # Use Tableau colors
    colors = {
        "Questions" : "tab:red",
        "Answers"   : "tab:blue"
    }

    plot.makeMultiPlot(df, plot_dir, plot_name, title, x_label, y_label, x_lim, y_lim, colors)

    print("Done!")

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
