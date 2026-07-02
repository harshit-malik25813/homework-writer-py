import datetime
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

date = datetime.datetime.now().strftime("%d-%m-%Y")
results.append(f"*Homework*\n\n{functions.text_bold(date)}\n")

for func in subjects:
    result = func()

    if result.strip():
        results.append(result)

print("\n".join(results))