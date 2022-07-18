'''
The adress of google spreadsheet where data is stored (PUBLIC ACCESS)
https://docs.google.com/spreadsheets/d/1ocMZYZez9pGDqUm6XyJ9FLx0B4dDI5fMG4sWjj87QJ4/edit#gid=757991760
'''
from oauth2client.service_account import ServiceAccountCredentials
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import gspread
import telebot
from datetime import datetime
import pandas as pd
bot = telebot.TeleBot('5315581483:AAECRxOUEKJCfBtv0N8u7ZC4cJJzt1o49tc')

record_dict = {}

#Google Sheet Authentication
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("aclassproject-355213-ccd229ffce0f.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open('Class info') # get the instance of the Spreadsheet



@bot.message_handler(commands=['start_bot'])
def send_welcome(message):
	keyboard = telebot.types.InlineKeyboardMarkup()  
	keyboard.row(telebot.types.InlineKeyboardButton('Повідомити про відсутність', callback_data='m1'))  
	keyboard.row(telebot.types.InlineKeyboardButton('Розклад занять', callback_data='m2')) 
	keyboard.row(telebot.types.InlineKeyboardButton('Дізнатись домашнє завдання', callback_data='m3')) 
	keyboard.row(telebot.types.InlineKeyboardButton('Відправити домашнє завдання', callback_data='m4')) 
	keyboard.row(telebot.types.InlineKeyboardButton('Розповісти вчителю як мої справи', callback_data='m5')) 
	bot.send_message(message.chat.id,  'Тебе вітає персональний помічник 4-А класу \U0001f600 \n Будь-ласка, вибери опцію:',  reply_markup=keyboard)


## Upload absense data to google sheets
@bot.callback_query_handler(func=lambda call: call.data == 'm1')
def callback_inline_second(call):
	sent = bot.send_message(call.message.chat.id, "Будь ласка, введи ПІБ відсутнього\nПриклад: Прощина Тетяна Андріївна")
	bot.register_next_step_handler(sent,absent_days)
    
    
def absent_days(message):
    absent_name = message.text
    record_dict["ПІБ"] = absent_name
    sent = bot.send_message(message.chat.id, "Будь ласка, введи к-сть днів відсутності\nПриклад: 1")
    bot.register_next_step_handler(sent,absent_date)
    
def absent_date(message):
    absent_days = message.text
    record_dict["Дні"] = absent_days
    sent = bot.send_message(message.chat.id, "Будь ласка, введи дату початку відсутності (у форматі - дд.мм.рррр)\nПриклад: 31.07.2022")
    bot.register_next_step_handler(sent,absence_reason)
    

def absence_reason(message):
    absent_date = message.text
    record_dict["Дата початку відсутності"] = absent_date
    sent = bot.send_message(message.chat.id, "Будь ласка, введи причину відсутності")
    bot.register_next_step_handler(sent,final_absence)
    
def final_absence(message):
    absent_reason = message.text
    record_dict["Причина відсутності"] = absent_reason
    print(record_dict)
    update_sheet(message)

def upload_data(worksheet,cell):
        cell_row = cell.row + 1
        cell_col = cell.col
        cell_val = worksheet.cell(cell_row, cell_col).value
        print(cell_val)
        while cell_val is not None:
            cell_row = cell_row + 1
            print(cell_row)
            cell_val = worksheet.cell(cell_row, cell_col).value
        print("Row {} is None".format(cell_row))
        worksheet.update_cell(cell_row, cell_col, record_dict['Дата початку відсутності'])
        worksheet.update_cell(cell_row,cell_col+1,record_dict['ПІБ'])
        worksheet.update_cell(cell_row,cell_col+2,record_dict['Дні'])
        worksheet.update_cell(cell_row,cell_col+3,record_dict['Причина відсутності'])

def update_sheet(message):
    worksheet = sheet.worksheet("Відсутність")
    cell = worksheet.find("Дата початку відсутності")
    upload_data(worksheet,cell)
    bot.send_message(message.chat.id,"Дякую, дані про відсутність успішно внесено")
    

## Get the schedule 
@bot.callback_query_handler(func=lambda call: call.data == 'm2')
def callback_inline_second(call):
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	start_markup.row('Понеділок', 'Вівторок', 'Середа')
	start_markup.row('Четвер', "П'ятниця")
	sent = bot.send_message(call.message.chat.id, "Будь ласка, обери день тижня, щоб дізнатися розклад", reply_markup = start_markup)
	bot.register_next_step_handler(sent, get_schedule)
	
def get_schedule(message):
	day = message.text
	worksheet = sheet.worksheet("Розклад занять")
	data = worksheet.get_all_values()
	headers = data.pop(0)
	df = pd.DataFrame(data, columns=headers)
	df = df[df['День'] == day]
	df = df[['Години','Предмет']]
	schedule = ''
	for index, row in df.iterrows():
		a = row['Години']
		b = row['Предмет']
		schedule += f"{a} {b}\n"
	sent = bot.send_message(message.chat.id, schedule)
	#print(df.head())
	
	
## Get the homework
homework_dict = {}

@bot.callback_query_handler(func=lambda call: call.data == 'm3')
def callback_inline_second(call):
	sent = bot.send_message(call.message.chat.id, "Будь ласка, введи дату, за яку хочеш дізнатися домашнє завдання (у форматі - дд.мм.рррр)\nПриклад: 31.07.2022")
	bot.register_next_step_handler(sent, get_subject)
	
def get_subject(message):
	date_ = message.text
	homework_dict["Дата"] = date_
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	start_markup.row('Математика', 'Українська мова', 'Англійська мова')
	start_markup.row('Трудове навчання', "Фізична культура", ' Всі предмети')
	sent = bot.send_message(message.chat.id, "Будь ласка, обери предмет", reply_markup = start_markup)
	bot.register_next_step_handler(sent, get_homework)
	
def get_homework(message):
	subject = message.text
	homework_dict["Предмет"] = subject
	worksheet = sheet.worksheet("Домашнє завдання")
	data = worksheet.get_all_values()
	headers = data.pop(0)
	df = pd.DataFrame(data, columns=headers)
	if homework_dict["Предмет"] == 'Всі предмети':
		try:
			df = df[df['Дата'] == homework_dict['Дата']]
			df = df[['Предмет','Завдання']]
			homework = ''
			for index, row in df.iterrows():
				a = row['Предмет']
				b = row['Завдання']
				homework += f"{a} - {b}\n"
			sent = bot.send_message(message.chat.id, homework)
		except telebot.apihelper.ApiException:
			data = homework_dict['Дата']
			sent = bot.send_message(message.chat.id, f'За {data} немає домашнього завдання')
	else:
		try:
			df = df[df['Дата'] == homework_dict['Дата']]
			df = df[df['Предмет'] == homework_dict['Предмет']]
			homework = ''
			for index, row in df.iterrows():
				b = row['Завдання']
				homework += f"{b}"
			sent = bot.send_message(message.chat.id, homework)
		except telebot.apihelper.ApiException:
			data = homework_dict['Дата']
			sub = homework_dict['Предмет']
			sent = bot.send_message(message.chat.id, f'За {data} по предмету {sub} немає домашнього завдання')



#Survey for students
survey_dict = {}
@bot.callback_query_handler(func=lambda call: call.data == 'm5')
def callback_inline_second(call):
	sent = bot.send_message(call.message.chat.id, "Вкажи своє ПІБ (Прізвище Ім'я та По-батькові)")
	bot.register_next_step_handler(sent,survey_2nd)

def survey_2nd(message):
	name = message.text
	survey_dict["name"] = name
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	start_markup.row('Так','Hi')
	sent = bot.send_message(message.chat.id, "Чи є в тебе комфортні умови для навчання і виконання домашніх завдань?",  reply_markup = start_markup)
	bot.register_next_step_handler(sent,survey_3rd)


def survey_3rd(message):
	question_1 = message.text
	survey_dict["question_1"] = question_1
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	start_markup.row('Так','Hi')
	sent = bot.send_message(message.chat.id, "Чи достатньо в тебе вільного часу для виконання домашніх завдань?",  reply_markup = start_markup)
	bot.register_next_step_handler(sent,survey_4th)
    
def survey_4th(message):
	question_2 = message.text
	survey_dict["question_2"] = question_2
	sent = bot.send_message(message.chat.id, "Будь ласка, залиш свій коментар, якщо хочеш чимось поділитись з вчителем")
	bot.register_next_step_handler(sent,survey_5th)
    
def survey_5th(message):
    question_3 = message.text
    survey_dict["question_3"] = question_3
    a = datetime.now()
    a = str(a.strftime('%d.%m.%Y'))
    survey_dict["Дата"] = a
    update_sheet2(message)

def upload_data2(worksheet,cell):
	cell_row = cell.row + 1
	cell_col = cell.col
	cell_val = worksheet.cell(cell_row, cell_col).value
	print(cell_val)
	while cell_val is not None:
		cell_row = cell_row + 1
		print(cell_row)
		cell_val = worksheet.cell(cell_row, cell_col).value
	print("Row {} is None".format(cell_row))
	worksheet.update_cell(cell_row, cell_col,survey_dict['name'])
	worksheet.update_cell(cell_row,cell_col+1,survey_dict['question_1'])
	worksheet.update_cell(cell_row,cell_col+2,survey_dict['question_2'])
	worksheet.update_cell(cell_row,cell_col+3,survey_dict['question_3'])
	worksheet.update_cell(cell_row,cell_col+4,survey_dict['Дата'])

def update_sheet2(message):
	worksheet = sheet.worksheet("Опитувальник для учнів")
	cell = worksheet.find("ПІБ")
	upload_data2(worksheet,cell)
	bot.send_message(message.chat.id,"Дякую, твої відповіді успішно внесено")



print("I'm listening...")
bot.infinity_polling()

