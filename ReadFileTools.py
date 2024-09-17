from langchain.tools import tool

class ReadFileTools():

    @tool("Read a file given file-name")
    def readFile(name):
        """Read a file
        """
        try:
            print("Read command is executed for file name:" + name)
            with open(name, 'r') as file:
                # Read the content
                content = file.read()
            print(content)
            # Return the content
            return content
        except Exception as e:
            return "Error: Invalid syntax in mathematical expression"