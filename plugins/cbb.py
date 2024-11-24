from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "menu":
        await query.message.edit_text(
            text = f"<b>ᴍᴇɴᴜ ꜰᴇᴀᴛᴜʀᴇᴅ</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🛒 ᴘʀᴏᴍᴏᴛɪᴏɴ ", callback_data="premium")
                 ],
              [InlineKeyboardButton("🔐 ᴘʀᴇᴍɪᴜᴍ ᴠɪᴘ ", callback_data='buy_prem'),
              InlineKeyboardButton("💰 ꜱᴛᴏʀᴇ ", callback_data='promotion')],
                    [InlineKeyboardButton('🌐 ᴡᴇʙꜱɪᴛᴇ ', url='https://px-z.blogspot.com')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )

    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"<blockquote>👋 hello user : {query.from_user.username}\n\n🎖️ Available Plans :\n\n● {PRICE1} rs For 7 Days Prime Membership\n\n● {PRICE2} rs For 1 Month Prime Membership\n\n● {PRICE3} rs For 3 Months Prime Membership\n\n● {PRICE4} rs For 6 Months Prime Membership\n\n● {PRICE5} rs For 1 Year Prime Membership\n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n♻️ If payment is not getting sent on above given QR code then inform admin, he will give you new QR code\n\n\n‼️ Must Send Screenshot after payment</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("Send Payment Screenshot(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )

    if data == "developer":
        await query.message.edit_text(
            text = f"<b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ʜʀʙᴛᴇᴀᴍ</a>\nꜱᴜᴘᴘᴏʀᴛ : <a href='https://t.me/HRBsupport'>ʜʀʙᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ</a>\nꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ : <a href='https://t.me/HRBsupport_official'>ʜʀʙᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ</a>\nꜱᴛᴏʀᴇ : <a href='https://t.me/HRBstore_official'>ʜʀʙꜱᴛᴏʀᴇ </a></b>",
           disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 1', url='https://t.me/dammingyu'),
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 2', url='https://t.me/Honorsteam')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ ', url='https://t.me/HRBsupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )

    elif data == "donate":
        await query.message.edit_text(
            text = f"<b>ᴅᴏɴᴀᴛᴇ - ʜʀʙꜰᴀᴍɪʟʏ</b>\nᴊɪᴋᴀ ᴋᴀʟɪᴀɴ ꜱᴜᴋᴀ ꜱᴀᴍᴀ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴋᴀᴍɪ ʙᴀɢɪᴋᴀɴ ꜱᴇᴄᴀʀᴀ ɢʀᴀᴛɪꜱ/ʙᴀʏᴀʀᴀɴ, ɪɴɢɪɴ ʙᴇʀʙᴀɢɪ (ᴅᴏɴᴀꜱɪ) ᴋᴇᴘᴀᴅᴀ ᴘxᴢᴛᴇᴀᴍ? ꜱɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ ᴠɪᴀ ᴅᴏɴᴀꜱɪ\n ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴛʜᴇ ᴠɪᴅᴇᴏꜱ ᴡᴇ ꜱʜᴀʀᴇ ꜰᴏʀ ꜰʀᴇᴇ/ᴘᴀɪᴅ, ᴡᴀɴᴛ ᴛᴏ ꜱʜᴀʀᴇ (ᴅᴏɴᴀᴛᴇ) ᴛᴏ ᴘxᴢᴛᴇᴀᴍ? ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴠɪᴀ ᴅᴏɴᴀᴛɪᴏɴ",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
              [  InlineKeyboardButton('🧾 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🧾 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')
          ],
                [  InlineKeyboardButton('🧾 ᴅᴀɴᴀ', url='https://t.me/PXZsub_bot?start=Z2V0LTE5MjE1MjcwODc1MDY5MDg'),
                InlineKeyboardButton('🧾 ᴛʀᴀᴋᴛᴇᴇʀ', url='https://trakteer.id/hrbofficial/tip')
          ],
                [  InlineKeyboardButton('🧾 ᴀʟɪᴘᴀʏ', url='https://t.me/PXZsub_bot?start=Z2V0LTE3NjcyNDM4OTA2OTk3ODQ')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )
    
    elif data == "premium":
        await query.message.edit_text(
            text = f"<b>ʟɪꜱᴛ ᴛᴏ ʙᴇ ᴘʀᴇᴍɪᴜᴍ ᴏꜰ ᴘxᴢᴠɪᴘ\n<blockquote>100 ᴠɪᴅᴇᴏ 5ᴋ\n200 ᴠɪᴅᴇᴏ 10ᴋ\n300 ᴠɪᴅᴇᴏ 15ᴋ\n400 ᴠɪᴅᴇᴏ 20ᴋ\n500 ᴠɪᴅᴇᴏ 25ᴋ\n600 ᴠɪᴅᴇᴏ 30ᴋ\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʙᴜʏ ᴠɪᴘ, ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ</blockquote></b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🔓 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🔓 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')],
                [InlineKeyboardButton('🛂 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/pxzstore_team')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
    elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴘʀᴏᴍᴏᴛɪᴏɴ ᴠɪᴅᴇᴏ/ᴘʜᴏᴛᴏ/ᴇᴛᴄ ᴄᴏɴᴛᴀᴄᴛ ꜱᴛᴏʀᴇ ᴛᴇᴀᴍ👇</b>",  disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/pxzstore_team'),
                InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://t.me/+U3RYX-jKJTxjYzk1')],
                [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
    )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
