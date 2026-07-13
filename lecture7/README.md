# Lecture 7 – Regular Expressions

## Overview

This lecture introduced regular expressions (regex), a powerful tool for searching, matching, validating, and extracting patterns from text.

Topics covered included:

* Pattern matching
* Character classes
* Quantifiers
* Capturing groups
* Non-capturing groups
* Optional groups
* Greedy vs non-greedy matching
* Word boundaries
* Input validation
* Data extraction from text
* Third-party validation libraries

Regular expressions initially felt difficult because of their syntax, but by the end of the lecture I was able to read, write, and debug moderately complex regex patterns.

---

## Problem Set 7

### NUMB3RS

Built a program that validates IPv4 addresses.

Concepts practiced:

* Capturing groups
* Anchors (`^` and `$`)
* Input validation
* Combining regex with logical checks

---

### Watch on YouTube

Built a program that extracts embedded YouTube URLs from HTML and converts them into shareable `youtu.be` links.

Concepts practiced:

* URL extraction
* Optional groups
* Non-capturing groups
* String reconstruction from regex matches

---

### Working 9 to 5

Built a program that converts 12-hour time formats into 24-hour time.

Concepts practiced:

* Optional regex groups
* Complex pattern matching
* Input validation
* Time conversion logic
* Exception handling

This was one of the most challenging exercises of the lecture because it combined regex with non-trivial business logic.

---

### Regular, um, Expressions

Built a program that counts occurrences of the word "um" while ignoring occurrences inside larger words.

Concepts practiced:

* Word boundaries (`\b`)
* Case-insensitive matching
* `re.findall`

---

### Response Validation

Built a program that validates email addresses using a third-party library.

Concepts practiced:

* External packages
* Input validation
* Understanding when to use existing libraries instead of writing everything from scratch

---

## Project – Study Log Parser

To reinforce the lecture, I built a Study Log Parser that converts natural-language study logs into structured CSV data.

### Example Input

```text
Today I studied Math for 2h 15m, Physics for 45m, and Python for 1h
```

### Generated Output

| Subject | Duration (minutes) |
| ------- | ------------------ |
| Math    | 135                |
| Physics | 45                 |
| Python  | 60                 |

### Concepts Practiced

* `re.sub`
* `re.finditer`
* Capturing groups
* Optional groups
* Non-capturing groups
* Data extraction
* CSV writing
* Data transformation pipelines

The program extracts study sessions from semi-structured text, converts durations into minutes, stores the results as dictionaries, and exports everything to a CSV file.

This project demonstrated how regular expressions can be used to transform messy human-written text into structured data.
