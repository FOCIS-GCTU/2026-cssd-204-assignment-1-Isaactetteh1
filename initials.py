# File: initials.py
# Description: Print out my initials I T J as large stylized block letters.
# Assignment Number: 1
#
# Name: Isaac Tetteh Junior
# STUDENT ID: 2425403361
# Email: 2425403361@live.gctu.edu.gh
# Grader: Augustus
#
# On my honor, Augustus Buckman, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print the small initials line with three periods and "ITJ"
    print()
    print("...ITJ")
    print()
    
    # Large period made of 4 asterisks
    period_row = "****"
    three_dots = "..."
    
    # Letter 'I' - 12 chars wide, 10 chars high (stylish block I)
    i0 = "IIIIIIIIIIII"
    i1 = "....II......"
    i2 = "....II......"
    i3 = "....II......"
    i4 = "....II......"
    i5 = "....II......"
    i6 = "....II......"
    i7 = "....II......"
    i8 = "....II......"
    i9 = "IIIIIIIIIIII"
    
    # Letter 'T' - 12 chars wide, 10 chars high (stylish block T)
    t0 = "TTTTTTTTTTTT"
    t1 = "....TT......"
    t2 = "....TT......"
    t3 = "....TT......"
    t4 = "....TT......"
    t5 = "....TT......"
    t6 = "....TT......"
    t7 = "....TT......"
    t8 = "....TT......"
    t9 = "....TT......"
    
    # Letter 'J' - 12 chars wide, 10 chars high (stylish block J)
    j0 = "JJJJJJJJJJJ."
    j1 = "........JJ.."
    j2 = "........JJ.."
    j3 = "........JJ.."
    j4 = "........JJ.."
    j5 = "........JJ.."
    j6 = "........JJ.."
    j7 = "JJ......JJ.."
    j8 = "JJ......JJ.."
    j9 = ".JJJJJJJ...."
    
    # Print all 10 rows - each row combines: ... + I + **** + ... + T + **** + ... + J
    # Row 0
    line0 = three_dots + i0 + period_row + three_dots + t0 + period_row + three_dots + j0
    print(line0)
    # Row 1
    line1 = three_dots + i1 + period_row + three_dots + t1 + period_row + three_dots + j1
    print(line1)
    # Row 2
    line2 = three_dots + i2 + period_row + three_dots + t2 + period_row + three_dots + j2
    print(line2)
    # Row 3
    line3 = three_dots + i3 + period_row + three_dots + t3 + period_row + three_dots + j3
    print(line3)
    # Row 4
    line4 = three_dots + i4 + period_row + three_dots + t4 + period_row + three_dots + j4
    print(line4)
    # Row 5
    line5 = three_dots + i5 + period_row + three_dots + t5 + period_row + three_dots + j5
    print(line5)
    # Row 6
    line6 = three_dots + i6 + period_row + three_dots + t6 + period_row + three_dots + j6
    print(line6)
    # Row 7
    line7 = three_dots + i7 + period_row + three_dots + t7 + period_row + three_dots + j7
    print(line7)
    # Row 8
    line8 = three_dots + i8 + period_row + three_dots + t8 + period_row + three_dots + j8
    print(line8)
    # Row 9
    line9 = three_dots + i9 + period_row + three_dots + t9 + period_row + three_dots + j9
    print(line9)
    
    # Print a blank line after the large initials
    print()


if __name__ == "__main__":
    main()
def main():
  pass #code goes here



main()
