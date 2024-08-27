from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from filters.chat_types import ChatTypeFilter

user_group_router = Router()

user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


listOfBadWords = set(['bad', 'word', 'badword','bad_word'])

@user_group_router.message(Command('menu'))
async def cmd_menu(message:Message):
    await message.answer('This is menu')
    
@user_group_router.message(F.text == 'hello')
async def answer_hello(message: Message):
    await message.reply(f'Hello, my friend {message.from_user.full_name}')

@user_group_router.edited_message()
@user_group_router.message()
async def delete_bad_words(message: Message):
    if listOfBadWords.intersection(set(message.text.lower().split(' '))):
        await message.delete()
        await message.answer('You can not use this word here')
    else:
        await message.answer('Your message is good')