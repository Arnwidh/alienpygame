class query:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#Här är frågor i en list
query_prompt = [
    "What is the name of the founder of Python?\n(1) Leonardo Davinci\n(2) Max\n(3) Guido Van Rossum\n\n",
    "What year was Python made?\n(1) 1987\n(2) 1991\n(3) 2004\n\n",
    "What happens if you type 'import this' into Python Idle?\n(1) A poem is printed\n(2) Nothing happens\n(3) You get an error message\n\n",
    "What is the origin behind the name Python?\n(1) It is the creators favorite animal\n(2) The comedy group Monty Python\n(3) No reason, creator thought it sounded cool\n\n",
    "What happens if you type 'import antigravity' into Python Idle?\n(1) Your computer loses gravity\n(2) A webcomic is opened\n(3) Nothing happens\n\n",
    "If you type 'Hello' 'World' '!' how will Python print it?\n(1) Hello World !\n(2) Hello_World_!\n(3) HelloWorld!\n\n"
    ""

]

queries = [
    query(query_prompt[0], "3"),
    query(query_prompt[1], "2"),
    query(query_prompt[2], "1"),
    query(query_prompt[3], "2"),
    query(query_prompt[4], "2"),
    query(query_prompt[5], "3"),
    query(query_prompt[6], ""),
    query(query_prompt[7], ""),
    query(query_prompt[8], ""),
    query(query_prompt[9], ""), 
]

def run_test(queries):
    score = 0
    for query in queries:
        answer = input(query.prompt)
        if answer == query.answer:
            score += 1
    
    print("You got " + str(score) + " out of " + str(len(queries)) + (" answers right."))

run_test(queries)