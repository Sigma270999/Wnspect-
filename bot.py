import telebot
import requests

API_TOKEN = '7900699121:AAHjeQ1mvx2wDzy6Mh-Gx7YNb3crxhT0tkE'  # Replace with your bot token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "🙏𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 ✨ Website Inspect Bot✨ 𝑾𝑬𝑩𝑺𝑰𝑻𝑬 💞𝑺𝑶𝑼𝑹𝑪𝑬 𝑪𝑶𝑫𝑬 𝑪𝑳𝑶𝑵𝑬𝑹 𝑩𝑶𝑻💞 🔥𝑺𝑬𝑵𝑫 𝑴𝑬 𝑨𝑵𝒀 𝑾𝑬𝑩𝑺𝑰𝑻𝑬 𝑳𝑰𝑵𝑲🔥")

@bot.message_handler(func=lambda message: True)
def fetch_source_code(message):
    url = message.text.strip()
    
    # Inform the user that the request is being processed
    processing_message = bot.send_message(message.chat.id, "🔥𝑷𝑳𝑬𝑨𝑺𝑬 𝑾𝑨𝑰𝑻 𝒀𝑶𝑼𝑹🔥 ✨𝑾𝑬𝑩𝑺𝑰𝑻𝑬 𝑺𝑶𝑼𝑹𝑪𝑬 𝑪𝑶𝑫𝑬✨ 𝑮𝑬𝑵𝑬𝑹𝑨𝑻𝑰𝑵𝑮 𝑩𝒀 @Inspectxurl_bot🔥...")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Save the source code to a file
        with open('source_code.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        # Send the source code file to the user
        with open('source_code.html', 'rb') as f:
            bot.send_document(message.chat.id, f)
        
        bot.send_message(message.chat.id, "✨𝒀𝑶𝑼𝑹 𝑺𝑶𝑼𝑹𝑪𝑬 𝑪𝑶𝑫𝑬 𝑮𝑬𝑵𝑬𝑹𝑨𝑻𝑰𝑵𝑮 ✨ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺𝑭𝑼𝑳 ✅")
    
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f"❌ Error fetching the source code: {str(e)}")
    
    finally:
        # Delete the processing message to clean up
        bot.delete_message(message.chat.id, processing_message.message_id)

if __name__ == "__main__":
    bot.polling(none_stop=True)
