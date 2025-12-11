# хотя я понимаю всё, что здесь написано,
# 80% этого кода написал ChatGPT

import csv
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

input_file = "input.csv"
output_file = "output.csv"

with open(input_file, newline='', encoding='utf-8') as infile, \
        open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:  # type: dict
        word = row.get("Слово", "")
        row["Лемма"] = morph.parse(word)[0].normal_form
        row["Часть речи"] = morph.parse(word)[0].tag.POS
        writer.writerow(row)
