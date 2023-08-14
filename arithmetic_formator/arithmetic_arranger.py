def arithmetic_arranger(problems):
  arranged_problems = ""
  
  for x in problems:
    A = ""
    B = ""
    C = ""
    D = 0
    flag_a = True
    flag_b = True

    for ch in x:
      if ch != ' ':
        if flag_a:
          A = A + ch
        elif flag_b:
          B = B + ch
        else:
          C = C + ch
      else:
        if flag_a:
          flag_a = False
        elif flag_b:
          flag_b = False

    if B[0] == '+':
      D = str(int(A) + int(C))
    else:
      D = str(int(A) - int(C))

    maxLen = max(len(A), len(C), len(D))
    
    while len(A) < maxLen:
      A = " " + A
    while len(C) < maxLen:
      C = " " + C
    while len(D) < maxLen:
      D = " " + D
    arranged_problems = arranged_problems + "  " + A + "\n"  
    arranged_problems = arranged_problems + B + " " + C + "\n"
    for i in range(maxLen + 2):
      arranged_problems = arranged_problems + "-"
    arranged_problems = arranged_problems + "\n"
    
  return arranged_problems
    

def arithmetic_arranger(problems, flag):
  if flag == False:
    return
  
  arranged_problems = ""
  
  for x in problems:
    A = ""
    B = ""
    C = ""
    D = 0
    flag_a = True
    flag_b = True

    for ch in x:
      if ch != ' ':
        if flag_a:
          A = A + ch
        elif flag_b:
          B = B + ch
        else:
          C = C + ch
      else:
        if flag_a:
          flag_a = False
        elif flag_b:
          flag_b = False

    if B[0] == '+':
      D = str(int(A) + int(C))
    else:
      D = str(int(A) - int(C))

    maxLen = max(len(A), len(C), len(D))
    
    while len(A) < maxLen:
      A = " " + A
    while len(C) < maxLen:
      C = " " + C
    while len(D) < maxLen:
      D = " " + D
    arranged_problems = arranged_problems + "  " + A + "\n"  
    arranged_problems = arranged_problems + B + " " + C + "\n"
    for i in range(maxLen + 2):
      arranged_problems = arranged_problems + "-"
    arranged_problems = arranged_problems + "\n"
    while len(D) < (maxLen + 2) :
      D = " " + D
    arranged_problems = arranged_problems + D + "\n"
  return arranged_problems