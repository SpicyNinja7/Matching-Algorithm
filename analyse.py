
preference_a = {
    "A":["1","2","4","3"],
    "B":["3","4","3","4"],
    "C":["1","3","4","2"],
    "D":["2","1","4","3"]
}
preference_b = {
    "1":["A","C","D","B"],
    "2":["A","D","C","B"],
    "3":["C","B","A","D"],
    "4":["D","A","B","C"]
}

matching={}
prev_matching={}
list_of_matched_sideB =[]
for a in preference_a.keys():
    matching[a]=''

while True:
    for a in preference_a.keys():
        prev_matching[a] = matching[a]

    #Group A's turn to choose
    for a in preference_a.keys():
        if matching[a]=='':
            matching[a]=preference_a[a][0]
            list_of_matched_sideB.append( matching[a])
            preference_a[a].pop(0)
    print("\nA Approaches B...")
    print(matching)

    #Group B's turn to choose
    for b in preference_b.keys():
        #removing duplicates of pairing to group B
        for a in preference_a.keys():
            if  matching[a] == b:
                if a != preference_b[b][0] and list_of_matched_sideB.count(b) >=2:
                    matching[a]=""

    #removing next choice of B if paired with A
    for a in preference_a.keys():
        if matching[a] == b:
            preference_b[b].pop(0)

    print("\nB rejects A...")
    print(matching)

    if prev_matching == matching:
        break

print("end of program")
