s = 'zyxwvutsrqponmlkjihgfedcba'

si = -1
new = False
big_sofar = ''
potentialbig_sofar = ''
right_ind = 0
left_ind = 0

for i in s:
    # increment to save the index of the current letter in the variable 'si'
    si += 1

    # checks if current letter comes before the next letter, alphabetically
    # it keeps building the longest substring as 'potentialbig_sofar' as long as 'new' is False.
    # guardian pattern to keep advancing if it's the same letter
    if s[si:si+1] < s[si+1:si+2] or s[si:si+1] == s[si+1:si+2]:
        if new == False:
            right_ind = si+1
        if new == True:
            left_ind = si
            new = False

        # sets the potentially biggest substring to be processed
        potentialbig_sofar = s[left_ind:right_ind+1]

        # processes whether the potential biggest substring is bigger than the old biggest substring
        if len(big_sofar) < len(potentialbig_sofar):
            big_sofar = potentialbig_sofar

    # initiate to build a new 'potentialbig_sofar'
    else: new = True

    # saves the first selected letter 'i' if 'big_sofar' never updates
    if len(big_sofar) == 0:
        big_sofar = i

print(big_sofar)