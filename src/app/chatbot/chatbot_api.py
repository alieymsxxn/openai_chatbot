from decouple import config
from openai import OpenAI, OpenAIError


class ChatGPTBotAPI:
    '''A class to interact with the OpenAI ChatGPT model.

    This class provides methods to manage prompts and retrieve responses from the ChatGPT model.
    It allows users to create, update, delete, and get responses for prompts stored in memory.
    The OpenAI API client is initialized using an API key from the environment configuration.

    Attributes:
        __prompts (list): A list of stored prompts for interaction with the ChatGPT model.
        __client (OpenAI): The OpenAI API client used to communicate with the GPT models.
    '''

    def __init__(self):
        self.__prompts = []
        self.__client = None

    @property
    def prompts(self):
        return self.__prompts

    @prompts.setter
    def prompts(self, value):
        if not isinstance(value, str):
            raise ValueError('Prompt must be a string.')
        self.__prompts.append(value)

    def initialize_gpt3(self):
        '''Initialize the OpenAI API client using the API key from the environment configuration.

        This method sets up the OpenAI client, allowing for interaction with the GPT models.
        It retrieves the API key from the environment variables using the decouple library.
        '''
        self.__client = OpenAI(api_key=config('API_KEY'))

    def __check_prompt_index(func):
        """Decorator to check if the provided prompt index is within the valid range.

        This decorator ensures that the prompt index passed to the decorated function
        is valid (i.e., not less than 0 and not greater than or equal to the number of stored prompts).

        Raises:
            IndexError: If the prompt index is out of range.
        """

        def wrapper(self, prompt_index, *args, **kwargs):
            if prompt_index < 0 or prompt_index >= len(self.prompts):
                raise IndexError('Prompt index out of range.')
            return func(self, prompt_index, *args, **kwargs)
        return wrapper

    def create_prompt(self, prompt):
        '''Store a user-provided prompt for later interactions.

        This method takes a string input as a prompt and appends it to the internal list of prompts.
        It ensures that the prompt is a valid string before storing it. This allows the user to 
        provide multiple prompts that can be referenced later for generating responses from the 
        ChatGPT model.

        Args:
            prompt (str): The prompt to be stored for future interactions.

        Returns:
            dict: A dictionary containing the stored prompt and its index.

        Raises:
            ValueError: If the provided prompt is not a string.
        '''
        self.prompts = prompt
        response = {
            'prompt': prompt,
            'prompt_index': len(self.prompts) - 1
        }
        return response

    @__check_prompt_index
    def get_response(self, prompt_index):
        '''Return the ChatGPT bot's response to a stored prompt.

        This method retrieves the response from the ChatGPT model for a specific prompt
        stored at the given index. It uses the OpenAI API client to generate the response
        based on the stored prompt and the model specified in the environment configuration.

        Args:
            prompt_index (int): The index of the prompt for which to get the response.

        Returns:
            dict: A dictionary containing the prompt and the generated response.

        Raises:
            IndexError: If the prompt index is out of range.
            Exception: For handling various OpenAI API exceptions.
        '''
        prompt = self.prompts[prompt_index]
        try:
            response = self.__client.chat.completions.create(
                model=config('MODEL', default='gpt-3.5-turbo'),
                temperature=config('TEMPERATURE', default=0.7),
                messages=[{'role': 'user', 'content': prompt}]
            )
            response = {
                'prompt': prompt,
                'reponse': response.choices[0].message.content
            }
            return response
        except OpenAIError as e:
            raise Exception(f"OpenAI API error: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    @__check_prompt_index
    def update_prompt(self, prompt_index, new_prompt):
        '''Update an existing prompt at the given index.

        This method allows the user to modify a previously stored prompt by providing
        a new string to replace the existing one at the specified index.

        Args:
            prompt_index (int): The index of the prompt to be updated.
            new_prompt (str): The new prompt string to replace the old one.

        Returns:
            dict: A dictionary containing the initial and final prompts.

        Raises:
            IndexError: If the prompt index is out of range.
        '''
        initial = self.prompts[prompt_index]
        self.prompts[prompt_index] = new_prompt
        response = {
            'inital': initial,
            'final': new_prompt
        }
        return response

    @__check_prompt_index
    def delete_prompt(self, prompt_index):
        '''Delete a prompt at the given index.

        This method removes the prompt stored at the specified index from the internal
        list of prompts, allowing for dynamic management of user-provided prompts.

        Args:
            prompt_index (int): The index of the prompt to be deleted.

        Returns:
            dict: A dictionary containing the deleted prompt and its index.

        Raises:
            IndexError: If the prompt index is out of range.
        '''
        deleted = self.prompts[prompt_index]
        del self.prompts[prompt_index]
        response = {
            'deleted_prompt': deleted,
            'deleted_prompt_index': prompt_index
        }
        return response
