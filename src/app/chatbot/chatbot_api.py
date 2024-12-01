from openai import OpenAI, RateLimitError
from decouple import config

class ChatGPTBotAPI:
    def __init__(self):
        self.prompts = []
        self.client = None

    def initialize_gpt3(self):
        '''Initialize the OpenAI API with the provided API key.'''
        self.client = OpenAI(api_key=config('API_KEY'))

    def check_prompt_index(func):
        def wrapper(self, prompt_index, *args, **kwargs):
            if prompt_index < 0 or prompt_index >= len(self.prompts):
                raise IndexError('Prompt index out of range.')
            return func(self, prompt_index, *args, **kwargs)
        return wrapper

    def create_prompt(self, prompt):
        '''Store a user-provided prompt for later interactions.'''
        self.prompts.append(prompt)

    @check_prompt_index
    def get_response(self, prompt_index):
        '''Return the ChatGPT bot's response to a stored prompt.'''

        response = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': self.prompts[prompt_index]}]
        )
        return response.choices[0].message.content

    @check_prompt_index
    def update_prompt(self, prompt_index, new_prompt):
        '''Update an existing prompt at the given index.'''
        
        self.prompts[prompt_index] = new_prompt

    @check_prompt_index
    def delete_prompt(self, prompt_index):
        '''Delete a prompt at the given index.'''
    
        del self.prompts[prompt_index]
