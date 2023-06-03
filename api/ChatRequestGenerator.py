import openai




class ChatRequestGenerator:
    def __init__(self, object_name: str):
        self.object_name = object_name
        self.list_of_objects = {
            'pszok': [
                'Środki ochrony osobistej',
                'Akumulatory i baterie',
                'Elektronika',
                'leki',
                'Tworzywa ',
                'Chemikalia',
                'odpadki budowlane',
                'styropian',
                'branżą motoryzacyjną',
                'mebel',

            ]
        }

    def _generate_request(self):
        list_of_obj_formatted = '\n'.join(self.list_of_objects.get('pszok'))
        self.request = f"Zapomnij o wszystkm. Teraz ty klasyfikujesz objecky. Mam liste: {list_of_obj_formatted}\nCzy {self.object_name} nalezy do kategorii podanych w liscie?\
        Odpowiedz tak albo nie. Jezeli nie, to zwroć do ktorej klasy nalezy obiekt."
        print(self.request)

    def make_request(self):
        self._generate_request()
        chat = ChatBot(self.request)
        response = chat.execute()
        return response


class ChatBot:
    def __init__(self, system):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        print(completion.usage)
        return completion.choices[0].message.content


