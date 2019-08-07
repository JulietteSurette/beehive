#Beehive



#BEE sounds
# "B" + "IY1" : "AUTOMOBILE", "BEE"
# "B" + "IY0" : AMPHIBIAN  [AE0 M F IH1 B IY0 AH0 N], AMPHIBIOUS  AE0 M F IH1 B IY0 AH0 S
# "B" + "IH1" : AMBITION      AE0 M B IH1 SH AH0 N
# "B" + "AH0" : UNBELIEVING  AH2 N B AH0 L IY1 V IH0 NG
# "B" + "IH0" : BELIEVE           B IH0 L IY1 V


#interesting cases:
# AMBIENT  AE1 M B IY0 AH0 N T
# AMBIGUITIES  AE0 M B AH0 G Y UW1 AH0 T IY0 Z
# AMBIGUITY  AE2 M B IH0 G Y UW1 AH0 T IY0
# AMBIGUOUS  AE0 M B IH1 G Y UW0 AH0 S
#

#make constant all CAPS : list
B_PHONETICS = ["IY1","IY0","IH1","IH0"]


# linesplit is a list
# e.g. ['zylka', 'Z', 'IH1', 'L', 'K', 'AH0']
def get_word(linesplit):
    word = linesplit[0] # word btwn "" bee
    # Write code here to get the word from the line linesplit and save it as 'word':
    return word

# return True if the list contains 'B' and 'IY1'
# linesplit is a list
# e.g. ['zylka', 'Z', 'IH1', 'L', 'K', 'AH0']
def has_bee_sound(linesplit):
    if "B" in linesplit:
        how_many_ducks = len(linesplit)
        get_Bindex = linesplit.index("B")
        if how_many_ducks -1 == get_Bindex:
            return False
        after_Bindex = get_Bindex +1
        phonetic_after_B = linesplit[after_Bindex]
        if phonetic_after_B in B_PHONETICS: #found first edgecase :)

            return True
    return False



# Create an empty dictionary
CMU_dict_aka_beehive = {}
# Load the text file_object
file_object  = open("CMU_dict_aka_beehive.txt", "r") #source: https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict

for line in file_object:
    # print line.split() #prints entire dictionary
    linesplit = line.split() #single row
    #print linesplit

    word = get_word(linesplit)
    if has_bee_sound(linesplit):
        print linesplit
