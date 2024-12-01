from flask import jsonify, request
from . import blueprint
from .chatbot_api import ChatGPTBotAPI
from .forms import CreateUpdatePromptForm

bot = ChatGPTBotAPI()
bot.initialize_gpt3()

@blueprint.route('/prompts', methods=['POST'])
def add_prompt():
    form = CreateUpdatePromptForm(request.form)
    if form.validate():
        bot.create_prompt(form.prompt.data)
        return jsonify({'message': 'Prompt added successfully.'}), 201
    return jsonify({'error': form.errors}), 400

@blueprint.route('/prompts/<int:prompt_index>/response', methods=['GET'])
def get_prompt_response(prompt_index):
    try:
        response = bot.get_response(prompt_index)
        return jsonify({'response': response}), 200
    except IndexError as e:
        return jsonify({'error': str(e)}), 400

@blueprint.route('/prompts/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    form = CreateUpdatePromptForm(request.form)
    if form.validate():
        try:
            bot.update_prompt(prompt_index=prompt_index, new_prompt=form.prompt.data)
            return jsonify({'message': 'Prompt updated successfully.'}), 200
        except IndexError as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': form.errors}), 400

@blueprint.route('/prompts/<int:prompt_index>', methods=['DELETE'])
def delete_prompt(prompt_index):
    try:
        bot.delete_prompt(prompt_index)
        return jsonify({'message': 'Prompt deleted successfully.'}), 200
    except IndexError as e:
        return jsonify({'error': str(e)}), 400
