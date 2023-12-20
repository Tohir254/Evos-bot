from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("6146304144:AAGRgRAe8Eghs2UALhM-W8ERr_E-ZsRpZBg")  # Bot toekn
# ADMINS = env.list([364603275])  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

BOT_TOKEN = '6680241557:AAEw11nC4rDGD6GNbio0fu86vAGG4MoQb14'
ADMINS = [5689522270]

DATABASE = {
    'NAME': 'evos_bot',
    'USER': 'postgres',
    'PASSWORD': '9090',
    'HOST': 'localhost',
    'PORT': '5432',
}

