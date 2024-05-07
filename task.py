import argparse
import random

BUCKET_SIZE = int(20) # The range for each bar (bucket) in the histogram "bar chart"
RANGE_MAX = int(100)

# Define the CLI argument options
def create_parser():
    parser = argparse.ArgumentParser(description="Command line app")
    parser.add_argument("-n", "--number", help="How many numbers the program should generate")
    return parser

# Generate an amount of numbers within the range of 0-99 (inclusive)
def generate_numbers(number_amount):
    numbers_list = [random.randint(0, 99) for x in range(number_amount)]
    return numbers_list

# Generate a histogram from a list of numbers
def generate_histogram(numbers_list):
    buckets_count = int(RANGE_MAX/BUCKET_SIZE) # Set number of buckets needed
    bucket_breakpoints = [(x+1)*BUCKET_SIZE for x in range(buckets_count)] # Set the breakpoints (bucket range max) for each bucket - e.g. 20, 40, 60, etc
    found_counts = []
    for x in bucket_breakpoints:
        current_min = x-BUCKET_SIZE # Reset bucket range min - e.g. 0-20, 20-40, 40-60, etc
        filtered_numbers = list(filter(lambda v: v in range(current_min, x), numbers_list)) # Filter the numbers found in numbers_list that fall within the bucket range
        found_counts.append(len(filtered_numbers)) # Add the count of the filtered numbers to found_counts
    for x in found_counts:
        print("*" * x) # Print *s for the number counts in the list (This is to create a histogram-like image, horizontally)

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.number:
        generate_histogram(generate_numbers(int(args.number))) # If the CLI argument for 'number' is passed, generate a histogram using the number given
    else:
        print("No argument provided.\nUse -h or --help for full usage options.")

if __name__ == "__main__":
    main()