# Python MapReduce with mrjob Library

A collection of MapReduce programs implemented using Python 3 and the mrjob library. This project demonstrates various MapReduce operations including finding maximum values, calculating means, analyzing URL paths, and word line indexing.

## Prerequisites

- Python 3.8.0 or higher
- pipenv (for dependency management)
- mrjob library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Python-MapReduce-mrjob-library.git
cd Python-MapReduce-mrjob-library
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

## Project Structure

The project consists of four MapReduce programs, each solving a specific problem:

### 1. Finding Maximum Value (`part1.py`)
Given a CSV file where each line contains a set of numbers, this program determines the maximum of all numbers in the file.

**Example Input:**
```
2,2,3
4,3
```

**Expected Output:** `4`

**Usage:**
```bash
pipenv run python part1.py input.csv
```

### 2. Calculating Mean (`part2.py`)
Given a CSV file where each line contains a set of numbers, this program calculates the mean of all numbers in the file.

**Example Input:**
```
2,2,3
4,3
```

**Expected Output:** `2.8`

**Usage:**
```bash
pipenv run python part2.py input.csv
```

### 3. Finding URL Paths (`part3.py`)
Given a CSV file where each line contains two URLs (source and destination), this program finds all paths of length two in the URL links.

**Example Input:**
```
url1,url2
url1,url3
url2,url3
url4,url5
url2,url4
```

**Expected Output:**
```
url2,url4,url5
url1,url2,url3
url1,url2,url4
```

**Usage:**
```bash
pipenv run python part3.py input.csv
```

### 4. Word Line Indexing (`part4.py`)
This program takes a file containing comma-separated words and outputs for each word the lines that contain it.

**Example Input:**
```
goat,chicken,horse
cat,horse
dog,cat,sheep
buffalo,dolphin,cat
sheep
```

**Expected Output:**
```
"buffalo" ["buffalo, dolphin, cat"]
"cat" ["buffalo, dolphin, cat", "cat,horse", "dog,cat,sheep"]
"chicken" ["goat,chicken,horse"]
"dog" ["dog,cat,sheep"]
"dolphin" ["buffalo,dolphin,cat"]
"goat" ["goat,chicken,horse"]
"horse" ["cat,horse", "goat,chicken,horse"]
"sheep" ["dog,cat,sheep", "sheep"]
```

**Usage:**
```bash
pipenv run python part4.py input.csv
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

  





