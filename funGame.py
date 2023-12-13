
def getInput(Word_type: str):
    userInput:str =input(f"Enter a {Word_type}")
    return userInput

noun1=getInput("noun")
verb1=getInput("verb")
noun2=getInput("noun")
verb2=getInput("verb")

story=f"""
the story is about {noun1}, where {noun2} has an important role to paly as vilion

git  has {verb1}to {noun2} 

{verb2} here

"""

print(story)