import functions
# Code to use the functions declared into formatting the hw for WhatsApp
subjects = [
    functions.maths,
    functions.phy,
    functions.chem,
    functions.bio,
    functions.sst,
    functions.hindi,
    functions.eng,
    functions.additional
]

results = []

date = functions.date()
results.append(f"*Homework*\n{date}")

for func in subjects:
    result = func()

    if result.strip():
        results.append(result)

print("\n".join(results))