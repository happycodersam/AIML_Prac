
facts = ["It is Raining"]
rules = {"It is Raining": "Road is Wet",
         "Road is Wet": "Road is Slippery"}

def forward():
    known = facts.copy()
    print("\nFORWARD CHAINING")
    changed = True
    while changed:
        changed = False
        for c, r in rules.items():
            if c in known and r not in known:
                print(c, "->", r)
                known.append(r)
                changed = True
    print("Final Facts:", known)

def backward(goal):
    if goal in facts:
        return True
    for c, r in rules.items():
        if r == goal:
            print("To prove:", goal, "\nNeed to prove:", c)
            return backward(c)
    return False

forward()
print("\nBACKWARD CHAINING")
goal = "Road is Slippery"
print("Goal Achieved!" if backward(goal) else "Goal Cannot Be Achieved")
