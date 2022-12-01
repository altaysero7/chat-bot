from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    'R2-D2',
    read_only=True,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I can only answer questions related to Star Wars.',
            'maximum_similarity_threshold': 0.90,
        },
    ],
    preprocessors=[
        "chatterbot.preprocessors.clean_whitespace",
    ],
    input_adaptor="chatterbot.input.TerminalAdaptor",
    output_adaptor="chatterbot.output.TerminalAdaptor",
)

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Hi",
    "What am I suppose to do here?",
    "Mmm... I don't know you came here :/",
    "What are you exactly?",
    "I am the master of AI!\nWould you like to ask me a question about Star Wars?",
    "Okay let's go",
    "I am warning you, I have so much knowledge :P",
    "What is Baby Yoda's real name?",
    "Grogu",
    "Where did Obi-Wan take Luke after his birth?",
    "Tatooine",
    "Who is Palpatine's granddaughter?",
    "Rey",
    "Who was Anakin Skywalker's Padawan?",
    "Ahsoka Tano",
    "What species is Chewbacca?",
    "Wookiee",
    "C-3PO is fluent in over how many forms of communication?",
    "Over six million",
    "Where does Rey find Luke Skywalker?",
    "Ahch-To",
    "Who killed Han Solo?",
    "Kylo Ren",
    "Ok I give up :(",
    "See! I told you :P",
    "I go bye!",
    "May the force be with you"
])

while True:
    try:
        user_input = input('>>> ').strip()
        if user_input != 'exit':
            print(chatbot.get_response(user_input).text)
        else:
            break
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
