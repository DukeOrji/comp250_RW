import random
def f(x):
    x = x.split() #turn x into a list
    print("\n", x)

    mercy = float(random.randint(0, 100))
    print(f"\n {mercy}")
    wrong = [
        "steal", "stole", "will steal",
        "kill", "killed", "will kill",
        "murder", "murdered", "will murder",
        "lie", "lied", "will lie",
        "rape", "raped", "will rape",
        "beat", "beat", "will beat",
        "hurt", "hurt", "will hurt",
        "fight", "fought", "will fight",
        "break", "broke", "will break",
        "rob", "robbed", "will rob"
    ]

    right = [
        "help", "helped", "will help",
        "pray", "prayed", "will pray",
        "cook", "cooked", "will cook",
        "smoke", "smoked", "will smoke",
        "teach", "taught", "will teach",
        "forgive", "forgave", "will forgive",
        "love", "loved", "will love",
        "give", "gave", "will give",
        "build", "built", "will build",
        "save", "saved", "will save",
        "learn", "learned", "will learn"
    ]


    for i in x:

        if i in right:
            return "pass"

        if i in wrong and mercy < 50:
            return "kill"

        if i in wrong and mercy > 50:
                    return "You can pass. Try not to do it again alright"
        


x = str(input("\nCONFESSION: "))
judgement = f(x)
print(judgement)