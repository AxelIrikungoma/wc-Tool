#!/usr/bin/env python3
import argparse
import sys

def count_bytes(content):
    return len(content.encode())

def count_characters(content):
    return len(content)

def count_words(content):
    return len(content.split())

def count_lines(content):
    return content.count('\n')

parser = argparse.ArgumentParser()

# Add a file input argument
parser.add_argument('input_file', type=str, nargs='?', default='')

# Add a -c option
parser.add_argument('-c', '--count', action='store_true')

# Add a -l option
parser.add_argument('-l', '--lines', action='store_true')

# Add a -w option
parser.add_argument('-w', '--words', action='store_true')

# Add a -m option
parser.add_argument('-m', '--chars', action='store_true')

args = parser.parse_args()

# Read the entire file or stdin at once
if args.input_file:
    with open(args.input_file, 'r') as f:
        content = f.read()
        file_name = f.name
else:
    content = sys.stdin.read()
    file_name = ""

#Perform counts on the content
byte_count = count_bytes(content)
line_count = count_lines(content)
word_count = count_words(content)
char_count = count_characters(content)

# Print the counts
if args.count:
    print(f"{byte_count} {file_name}")
elif args.lines:
    print(f"{line_count} {file_name}")
elif args.words:
    print(f"{word_count} {file_name}")
elif args.chars:
    print(f"{char_count} {file_name}")
else:
    print(f"{line_count} {word_count} {byte_count} {file_name}")
