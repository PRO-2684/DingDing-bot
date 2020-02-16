from bot import bot
my_bot = bot(input("Robot's keyword: "), input("Your token: "))
my_bot.send_text('Hello world!')
my_bot.send_text('Test#at', at=[input("Enter the phone number of someone you'd like to @: ")])
my_bot.send_text('Test#atAll', atAll=True)
