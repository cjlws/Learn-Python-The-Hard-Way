
formatter = "%r %r %r %r" # assigns a string to variable 'formatter'
                          # consisting of four commands to dump the
                          # passed in information in raw format

print formatter % (1, 2, 3, 4) # should print out the string '1 2 3 4'
print formatter % ("one", "two", "three", "four") # should print out the string "'one' 'two' etc"
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
