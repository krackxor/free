    # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Catatan: Mode aktif ✅\n\n__Beri aku keterangan untuk diatur.__\n\nContoh:- `/set_caption {filename}\n\n💾 Ukuran: {filesize}\n\n⏰ Durasi: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__** CAPTION ANDA BERHASIL DISIMPAN ✅**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("Catatan: Mode aktif ✅\n\n😔**Maaf! Teks tidak ditemukan...**😔")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**** Teks Anda berhasil dihapus**✅️")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Catatan: Mode aktif ✅\n\nTeks Anda:-**\n\n`{caption}`")
    else:
       await message.reply_text("😔**Maaf ! Teks tidak ditemukan...**😔")
