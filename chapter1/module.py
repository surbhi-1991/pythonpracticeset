import pyjokes


jokes = []


for i in range(0,10):
    joke = pyjokes.get_joke()
    jokes.append(joke)


for i in range(0,10):
    print(f'Current joke is -> {jokes[i]}')



