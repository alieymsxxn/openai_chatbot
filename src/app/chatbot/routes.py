from flask import jsonify, request
from . import blueprint
from .chatbot_api import ChatGPTBotAPI
from .forms import CreateUpdatePromptForm

bot = ChatGPTBotAPI()
bot.initialize_gpt3()


@blueprint.route('/prompts', methods=['POST'])
def add_prompt():
    '''Add a new prompt to the chatbot.

    Params:
        None: Expects prompt data in the request body.

    Response:
        JSON object with a success message or error details.
    '''
    form = CreateUpdatePromptForm(request.form)
    if form.validate():
        prompt_data = bot.create_prompt(form.prompt.data)
        response = {
            'message': 'Prompt added successfully.',
            'response': prompt_data
        }
        return jsonify(response), 201
    return jsonify({'error': form.errors}), 400


@blueprint.route('/prompts/<int:prompt_index>/response', methods=['GET'])
def get_prompt_response(prompt_index):
    '''Retrieve the response for a specific prompt by its index.

    Params:
        prompt_index (int): The index of the prompt to retrieve the response for.

    Response:
        JSON object containing the response from the chatbot or error details.
    '''
    try:
        response_data = bot.get_response(prompt_index)
        response = {
            'message': "Response successfully generated.",
            'response': response_data
        }
        return jsonify(response), 200
    except IndexError as e:
        return jsonify({'error': str(e)}), 400


@blueprint.route('/prompts/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    '''Update an existing prompt at the specified index.

    Params:
        prompt_index (int): The index of the prompt to be updated.

    Response:
        JSON object with a success message or error details.
    '''
    form = CreateUpdatePromptForm(request.form)
    if form.validate():
        try:
            update_data = bot.update_prompt(prompt_index=prompt_index,
                                            new_prompt=form.prompt.data)
            response = {
                'message': "Update has been successfully.",
                'response': update_data
            }
            return jsonify(response), 200
        except IndexError as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': form.errors}), 400


@blueprint.route('/prompts/<int:prompt_index>', methods=['DELETE'])
def delete_prompt(prompt_index):
    '''Delete a prompt at the specified index.

    Params:
        prompt_index (int): The index of the prompt to be deleted.

    Response:
        JSON object with a success message or error details.
    '''
    try:
        deletion_data = bot.delete_prompt(prompt_index)
        response = {
            'message': 'Prompt has been deleteed',
            'response': deletion_data
        }
        return jsonify(response), 200
    except IndexError as e:
        return jsonify({'error': str(e)}), 400
