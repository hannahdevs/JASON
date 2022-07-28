# JASON
A tiny python utility for dictionary based find and replace in a single string based file.

## Instructions

Create a `.csv` to serve as the glossary with the first line `Property,Value`. Alternatively you could use a spreadsheet software and export as a csv, so long as your first row is correct.

Example:
```
Property,Value
Name,Hannah
Instagram,http://instagram.com/example
Phone,123-456-7890
Favorite Food,Sushi
```

Then, In a string based file, refer to those items by their property name using double curly brackets.

Example:
```
Hello {{Name}},
I also love {{Favorite Food}}.
```

Load these two files into JASON and click `Run`.

## Process
1. Takes two files as input.
2. Loads selected csv file to a "glossary"
3. Loops through the glossary and performs find and replace.
4. Writes changes to a new file.

## Inputs

| File  | Details |
| ------------- |:-------------:|
| CSV     | First line must be `Property,Value`     |
| Input      | String based input file of any kind.     |

## Outputs

| File  | Details |
| ------------- |:-------------:|
| Input`.j`     | Copy of the Input file where all instances of keys in the glossary have been replaced with their corresponding values. Appended with `.j` extension|

## Plans
- Add functionality to run JASON through multiple files.
- Add functionality to append a write to the output file for each key value pair in the glossary.
- Allow the above to be in a single or multiple files.
