import random
from string import punctuation
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if (len(tokens) - 1) == i:
                break
            self.graph[token].append(tokens[i + 1])

    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            nextWord = random.choice(options)
            # add the random choice to the output string
            output = output + " " + nextWord
            current = nextWord
        return output

######################################################################################################################33

text = """Computer science is the study of computation, information, and automation.[1][2][3] Computer science spans theoretical disciplines (such as algorithms, theory of computation, and information theory) to applied disciplines (including the design and implementation of hardware and software).[4][5][6]

Algorithms and data structures are central to computer science.[7] The theory of computation concerns abstract models of computation and general classes of problems that can be solved using them. The fields of cryptography and computer security involve studying the means for secure communication and preventing security vulnerabilities. Computer graphics and computational geometry address the generation of images. Programming language theory considers different ways to describe computational processes, and database theory concerns the management of repositories of data. Human–computer interaction investigates the interfaces through which humans and computers interact, and software engineering focuses on the design and principles behind developing software. Areas such as operating systems, networks and embedded systems investigate the principles and design behind complex systems. Computer architecture describes the construction of computer components and computer-operated equipment. Artificial intelligence and machine learning aim to synthesize goal-orientated processes such as problem-solving, decision-making, environmental adaptation, planning and learning found in humans and animals. Within artificial intelligence, computer vision aims to understand and process image and video data, while natural language processing aims to understand and process textual and linguistic data.

The fundamental concern of computer science is determining what can and cannot be automated.[2][8][3][9][10] The Turing Award is generally recognized as the highest distinction in computer science.[11][12]"""

chain = MarkovChain()
chain.train(text)
sample_prompt = "Science is"
print(chain.generate(sample_prompt))