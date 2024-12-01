from chatbot_api import ChatGPTBotAPI


bot = ChatGPTBotAPI()
bot.initialize_gpt3()
bot.create_prompt('What is the capital of Pakistan?')
bot.get_response(0)
pass