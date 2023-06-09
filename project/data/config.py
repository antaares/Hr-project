from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
admins_ = env.list("ADMINS")
ADMINS = [int(admin) for admin in admins_]  # Adminlar ro'yhati




owner = -1001870806949