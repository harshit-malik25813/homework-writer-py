def maths():
    hw = input("What is the Maths homework?")
    final = ""
    if hw:
        final = f"*Maths*: {hw}"
    return final
def phy():
    hw = input("What is the Physics homework?")
    final = ""
    if hw:
        final = f"*Physics*: {hw}"
    return final
def chem():
    hw = input("What is the Chemistry homework?")
    final = ""
    if hw:
        final = f"*Chemistry*: {hw}"
    return final
def bio():
    hw = input("What is the bio homework?")
    final = ""
    if hw:
        final = f"*Biology*: {hw}"
    return final
def sst():
    hw = input("What is the SST homework?")
    final = ""
    if hw:
        final = f"*SST*: {hw}"
    return final
def hindi():
    hw = input("What is the Hindi homework?")
    final = ""
    if hw:
        final = f"*Hindi*: {hw}"
    return final
def eng():
    hw = input("What is the English homework?")
    final = ""
    if hw:
        final = f"*English*: {hw}"
    return final
def date():
    date_string = input("Enter the date: ")
    if date_string == "":
        date_string = date()
    date_string = f"*{date_string}*"
    return date_string
def additional():
    additional = input("Tell any additional details needed: ")
    return additional

