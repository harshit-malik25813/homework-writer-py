def maths():
    hw = input("What is the Maths homework?")
    final = ""
    if hw:
        final = f"*Maths*: {hw}\n"
    return final
def phy():
    hw = input("What is the Physics homework?")
    final = ""
    if hw:
        final = f"*Physics*: {hw}\n"
    return final
def chem():
    hw = input("What is the Chemistry homework?")
    final = ""
    if hw:
        final = f"*Chemistry*: {hw}\n"
    return final
def bio():
    hw = input("What is the bio homework?")
    final = ""
    if hw:
        final = f"*Biology*: {hw}\n"
    return final
def sst():
    hw = input("What is the SST homework?")
    final = ""
    if hw:
        final = f"*SST*: {hw}\n"
    return final
def hindi():
    hw = input("What is the Hindi homework?")
    final = ""
    if hw:
        final = f"*Hindi*: {hw}\n"
    return final
def eng():
    hw = input("What is the English homework?")
    final = ""
    if hw:
        final = f"*English*: {hw}\n"
    return final
def additional():
    additional = input("Tell any additional details needed: ")
    return additional
def text_bold(Str: str):
    return f"*{str}*"


