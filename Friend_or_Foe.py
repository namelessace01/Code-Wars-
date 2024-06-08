# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
# Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# i.e: friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

def friend(x):
    output = []
    for i in x:
        if len(i) == 4:
            output.append(i)
    return output
    
    
print(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])

# OR

def friends(x):
    return [output for output in x if len(x) == 4]
    # Although it's not so effective as the first one
    # It all balls down to personal ideals eventually