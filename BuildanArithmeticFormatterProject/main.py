def arithmetic_arranger(problems,   show_answers=False):
    str_result = ""
    opnd1 = ""
    opnd2 = ""
    space = " "*4
    dashes = ""
    maxOp = []
    errorCount = 0
    for index, s in enumerate(problems, start = 1):        
        s = s.split()   
        s2 = s[2]   # Error: Numbers cannot be more than four digits. 'Error: Numbers must only contain digits.'
        op = s[1]   # Operator must be '+' or '-'."
        s1 = s[0]   # Numbers cannot be more than four digits. 'Error: Numbers must only contain digits.'
        
        if  not s[0].isdigit(): return('Error: Numbers must only contain digits.')        
        if len(s[0]) > 4 : return("Error: Numbers cannot be more than four digits.")    
        if  not s[2].isdigit(): return('Error: Numbers must only contain digits.')        
        if len(s[2]) > 4 : return("Error: Numbers cannot be more than four digits.")        
        if  not (op == '+' or op == '-'): return("Error: Operator must be '+' or '-'.")
        if index > 5: return('Error: Too many problems.') 
        
        int_s1 = int(s[0])
        int_s2 = int(s[1]+s[2])
        int_result = int_s1 + int_s2
        s_result = str(int_result)
        
        padding = max(len(s1), len(s2))
        str1 = s1.rjust(padding + 2)
        str2 = op + ' ' + s2.rjust(padding)
        st_result = s_result.rjust(padding + 2)
        
        if index < len(problems):
            opnd1 = opnd1+str1+space
            opnd2 = opnd2+str2+space
            dashes = dashes+"-"*(padding+2)+space
            str_result = str_result+st_result+space        
        else: 
            opnd1 = opnd1+str1
            opnd2 = opnd2+str2
            dashes = dashes+"-"*(padding+2)
            str_result = str_result+st_result
    
    if show_answers: problems =  (opnd1+'\n'+opnd2+'\n'+dashes+'\n'+str_result)
    else: problems = (opnd1 +'\n'+opnd2+'\n'+dashes)
    return problems

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))