from bot import bot
my_bot = bot('YOUR_TOKEN', secret='YOUR_SECRET')
t = input('Text')
md = f"""# {t}"""
my_bot.send_md(t, md)
