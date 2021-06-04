# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt


def is_valid_email_address(s):

    num_at = s.count('@')
    if num_at != 1:
        return 8, "Email address must contain one @"


    AB = s.split('@')
    A = AB[0]
   
    postAt = AB[1].split('.')
    num_dot = AB[1].count('.')
    if num_dot != 1:
      return 9, "Post @ must contain a ."
      
    B = postAt[0]
    C = postAt[1]
    
    # Part A
    if len(A)<3:
        return 1, "\"" + A + "\"" + " is too short. It must contain more than 3 alpha numeric characters"
    if len(A)>16:
        return 2, "\"" + A + "\"" + " is too long. It must contain less than 16 alpha numeric characters"
    if A.isalnum() == False:
        return 6, "\"" + A + "\"" + " is not valid. Email cannot contain any special characters."


    # Part B
    if len(B)<2:
        return 3, "\"" + B + "\"" + " is too short. It must contain more than 2 alpha numeric characters"
    if len(B)>8:
        return 4, "\"" + B + "\"" + " is too long. It must contain less than 8 alpha numeric characters"
    if B.isalnum() == False:
        return 7, "\"" + B + "\"" + " is not valid. Email cannot contain any special characters."

    # Part C
    if C not in ["com", "edu", "org", "gov"]: 
        return 5, "\"." + C + "\"" + " is not valid. Email address must be a .com, .gov, .edu, or .org"

    # If s passes all tests
    return None, "Seems legit."

# print(is_valid_email_address("chris.edu"))

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(f"error code: {r} ({e}) --> {s}") # OK
        else:
            print(f"error code: {r} ({e}) --> {s}") # Error

        
