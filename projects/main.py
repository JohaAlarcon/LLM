import os

print("hello LangChain")

def my_function():
    print(os.environ['OPENAI_API_KEY'])

if __name__ == '__main__':
    my_function()