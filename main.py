from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

api_id = "20960397"
api_hash = "d68d847d3abb2087bf74f5d0683c2993"
bot_token = "6280228398:AAFZQprb6QBBy_FuYwbZwUdf_q9QIbrP-dI"

app = Client(
    "app",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

# Define the callback function for the "start" command
@app.on_message(filters.command("start"))
def start_command(client, message):
    # Send a welcome message
    client.send_message(chat_id=message.chat.id, text="Hiii, welcome to test bot")

    # Create an inline keyboard markup with a "help" button
    keyboard = [[InlineKeyboardButton("Help", callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the inline keyboard markup with the "help" button
    client.send_message(chat_id=message.chat.id, text="How can I help you?", reply_markup=reply_markup)

# Define the callback function for the inline keyboard buttons
@app.on_callback_query()
def button(client, callback_query):
    if callback_query.data == 'help':
        # Respond to the "help" button
        callback_query.answer("Here's how I can help you:\n- Type /start to get a welcome message and an inline keyboard markup.")

# Start the bot
app.run()
