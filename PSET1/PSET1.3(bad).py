s = 'azcbobobegghakl'

si = -1
h_sofar = ''
hi_sofar_l = None
hi_sofar_r = None
new = True
bnew = False
biggest = ''
p_biggest = ''

for i in s:
    si += 1

    if s[si:si+1] < s[si+1:si+2]:
        if new == True: hi_sofar_l = si
        hi_sofar_r = si+2
        p_biggest = s[hi_sofar_l:hi_sofar_r]
        new = False 
        
        if len(biggest) < len(s[hi_sofar_l:hi_sofar_r]):
            biggest = s[hi_sofar_l:hi_sofar_r]
        
        if bnew == True and len(biggest) < len(p_biggest):
            biggest = p_biggest
        continue
    else:
        bnew = True
    
print(s[hi_sofar_l:hi_sofar_r])
        