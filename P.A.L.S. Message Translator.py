#P.A.L.S. Message Translator Ver 1.0
#'Handle with care' --- Pat C

letter_to_number = {
"a" : 1,
"b" : 2,
"c" : 3,
"d" : 4,
"e" : 5,
"f" : 6,
"g" : 7,
"h" : 8,
"i" : 9,
"j" : 10,
"k" : 11,
"l" : 12,
"n" : 14,
"o" : 15,
"p" : 16,
"q" : 17,
"r" : 18,
"s" : 19,
"t" : 20,
"u" : 21,
"v" : 22,
"w" : 23,
"x" : 24,
"z" : 26,
"A" : 27,
"B" : 28,
"C" : 29,
"E" : 31,
"F" : 32,
"G" : 33,
"I" : 35,
"J" : 36,
"K" : 37,
"N" : 40,
"O" : 41,
"P" : 42,
"Q" : 43,
"S" : 45,
"T" : 46,
"U" : 47,
"W" : 49,
"X" : 50,
"Y" : 51,
"Z" : 52,
"," : 53,
"." : 54,
" " : 55
}

number_to_letter = {value: key for key, value in letter_to_number.items()}

with open(r"F:\ProgramReliantFiles\message.txt", "r") as f:
    text = f.read().strip("[]")
    numbers = text.split("#")

translated = []
for n in numbers:
    translated.append(number_to_letter.get(int(n)))

print("[" + "".join(translated) + "]")