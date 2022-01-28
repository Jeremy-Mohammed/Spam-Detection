# CSCI 1030U Practice Final Exam - Programming Question #1

def processHTML(filename, handleContent):
    with open(filename, 'r') as file:
        fileContents = file.read()
        inContent = False 
        content = ''
        for character in fileContents:
            if inContent and character == '<':
                handleContent(content)
                content = ''
                inContent = False
            elif not inContent and character == '>':
                inContent = True
            elif inContent:
                content += character

def printContent(content):
    print(content)

processHTML('sample.html', printContent)
