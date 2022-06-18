import discord
from discord import utils
from discord import client
import config
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from threading import Thread
import random
import io
import asyncio
import requests
import time

Y = 14
en = ['try again','i am not working right now','let`s go play','i don`t know how to talk','I am playing the game','egg or chicken?','my stupid neural network cannot process so much information','i can`t speak','Programmers update addresses in my memory','sorry but I`m busy','how are you?','Hello!']
bad_f = ['ахуе','idiot','lox','noob','хуй','залупа','бля','сосать','пизда','пидор','пидар','сук','долбае','ебл','пидр','дроч','cyk','уебки','СОСАТЬ','Шлюха','уеба','Сосать','сосать','Сук','Бля','Уебк','Пидр','Пидар','Пизда','Хуй']
stihi = ['Долго сделать кран просила\nСвоего я дурака,\nПлюнула, сама сменила -\nКран, замок и... мужика!','Жить порой не хочется, а надо...\nТы поверь совету старика:\nЕсли захотелось выпить яда...\nВыпей для начала коньяка...','Если дама выглядит прекрасно,\nИ одета модно и обута,\nТо, конечно, это не напрасно,\nВероятно дама мстит кому-то!','Ну, в общем, я живу и не скучаю!\nДарю я радость, ласку и покой!\nИ на добро - добром я отвечаю...\nНу, а на гадость - тем, что под рукой...']
ban=['1см','1.5см','2см','2.5см','3см','3.5см','4см','4.5см','5см','5.5см','6см','6.5см','7см','8см','9см','10см','10.5см','11см','11.5см','12см','12.5см','13см','13.5см','14см','14.5см','15см','15.5см','16см','17см','18см','19см','20см','21см','22см']
govor = ['вилкой в глаз или ...','Курица или яйцо?','Моя глупая нейросеть не может обрабатывать настолько большой объем информации','Дай в доту поиграть!','Я немой','Подожди программисты обновляют адреса в моей памяти','мужик, не нарывайся на проблемы...','Давай поиграем в игру «Как достать админа» \np.s. если тебя забанят я ничего не знаю)','Я хочу Питсы','Если нажать клавиши Alt+F4 то я могу активировать тебе мод Админа на 360 дней...','Тебе скучно? Ну так меня не заёбуй!','Как дела? У меня збс работаю на этот Чертов сервер...']
shutki = ['По улице шли две девушки - одна красивая, другая даст.','Настоящая бедность - это когда жену берешь в ипотеку.','Девушка, давшая обещание не есть после шести, выпила котлету.','У хорошего отца не может быть любимчиков. Все дети должны получать одинаковые алименты.','Если на сольный концерт пришло мало людей, то это малосольный концерт.','Обидно, когда привозишь вирус из Италии, а он все равно сделан в Китае.','Мало кто знает, но сиамские близнецы бьются яйцами не только на пасху.','А спонсор сервера Ураган в доме престарелых - ураган в доме пристарелых бабки на ветер','Отправил девушке смс “Этот абонент просит Вас выйти за него замуж”…получил ответ “Уважаемый абонент! На вашем счёте недостаточно средств для данной операции','Зая, хочешь, я для тебя достану звезду? — Опять будешь в три часа ночи названивать Киркорову?','Как называют человека у которого нету левой руки и левой ноги?All Right','Почему толстых женщин не берут работать стриптезершами?\n-Они перегибают палку.','Мама спросила у деда:\nЗачем тебе граната?\nОтвет взорвал.','Сидит маленький мальчик на траве возле сломанной машинки и плачет , тут к нему подходит наркоман:\n-Чего плачешь?\n-Да колеса потерял(\n-Так пошли я тебе свои дам\n-Не могу мне мама сказала на травке сидеть!\n-Эх мне бы такую маму(','Час ночи в украине и маленький мальчик не спит. Встает идет в комнату к деду и говорит:\n-Діду а в тебе була на війні щабля?\n-Що б**?\n-Та спи б**']
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
client = discord.Client()
@bot.event
async def on_ready():
	print("------------------------------\n\n\nNAEO Command bot has been run!\n\n\n------------------------------")
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('CS:GO'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Fortnite'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Dota2'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Pubg'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Minecraft'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('CS:GO'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Fortnite'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Dota2'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Pubg'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Minecraft'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('CS:GO'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Fortnite'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Dota2'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Pubg'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Minecraft'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('CS:GO'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Fortnite'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Dota2'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Pubg'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Minecraft'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('CS:GO'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Fortnite'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Dota2'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Pubg'))
	await asyncio.sleep(3600)
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Minecraft'))
	await asyncio.sleep(3600)
@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    for i in bad_f:
        if i in msg.content:
            await msg.delete()
@bot.command(pass_context=True)
async def help(ctx,*args):
    retStr = str("""```fix\nПривет. Тебе тут нужна помощь?Я сам не много знаю но помочь постараюсь!\n1.Для полученияя ролей нужно быть активным\n2.Обижают пиши Админам\n3.Замутили микрофон пиши всемогущему Админу в лс \n4.У каждой привилегии есть свой дополнительный чат\n5.Чтоб просмотреть список команд введи !list\n6.!info о сервере\n\n\nHey. Do you need help here? I don’t know much myself, but I’ll try to help! \n1.To get roles, you need to be active\n2.If somebody mute your microphone, write to the almighty Admin in hp \n3.Each privilege has its own additional chat \n4. To view the list of commands enter !command \n5.!information about the server```""")
    embed = discord.Embed(title="Help",colour=discord.Colour.orange())
    embed.add_field(name="Помощь",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def pogovori(ctx):
    retStr = (random.choice(govor))
    embed=discord.Embed(title="Стих",colour = discord.Colour.orange())
    embed.add_field(name="ну посмотрим",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('{}Я тебе ща кабину розвалю!А это ты. Ну проходи'.format(ctx.message.author.mention))
@bot.event
async def on_member_join(member:discord.Member):
    chan = member.guild.categories[0]
    channel = chan.channels[0]
    retStr = str(f"""```\nПривет *{member}*!\nРад приветствовать тебя на {member.guild}!\nЕсли с чем то не сможешь разобратся пиши !help.Скажу по секрету все команды на сервере начинаются с !\nВ чате языка выбери себе язык клиента сервера)\nНадеюсь тебе тут понравится)\n\n\nEnglish:\nHello *{member}*\nGlad to welcome you to **{member.guild}**\nIf something is not clear,write !help\nIn language chat choose your server client language)\nI hope you like it here!```""")
    embed = discord.Embed(title="▁▂▃▅▆█ 𝕡 𝕣 𝕚 𝕧 𝕖 𝕥 █▆▅▃▂▁",colour=discord.Colour.blue())
    embed.add_field(name="Новый молодой на сервере",value=retStr)
    await channel.send(embed=embed)
    new_role = discord.utils.get(member.guild.roles,name = 'Новичок')
    liga_role = discord.utils.get(member.guild.roles,name = '🎍Лига новобранцев')
    await member.add_roles(new_role)
    await member.add_roles(liga_role)
@bot.event
async def on_member_remove(member:discord.Member):
    message = member.guild.categories[0]
    mes = message.channels[1]
    retStren = str(f"""```\nOps *{member}* left {member.guild}!\n{member} come back to us yet!```""")
    embed = discord.Embed(title="▁▂▃▅▆█ 𝕓𝕪𝕦 █▆▅▃▂▁",colour=discord.Colour.blue())
    embed.add_field(name="Leave server",value=retStren)
    await mes.send(embed=embed)
@bot.command(pass_context=True)
async def банан(ctx):
	x = random.choice(ban)
	ch = x
	await ctx.send(ch)
	await ctx.send('твой банан {} '.format(ctx.message.author.mention))
	if str(ch) > str(Y) :
		await ctx.send('Не плохо')
	else:
		await ctx.send('Маловат')
@bot.command(pass_context=True)
async def bun(ctx):
	retStr =  ("""```excel\nББББББББББББААААААААААААННННННННН\n  ```""")
	embed=discord.Embed(title="БААААН",colour = discord.Colour.red())
	embed.add_field(name="БАН",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def rule(ctx):
	retStr = ("""```Привет!\nНу давай посмотрим правила\n\n\n1.На сервере нельзя матерится за этим буду следить я или если ты найдешь способ написать тебя замутят модераторы или же администраторы)\n2.Префикс к нику ⓃⒶⒺⓄ может использовать только Администрация и модераторы\n3.Обижать других тоже не желательно\n4.Вас не имеют права замутить просто так если такое произошло то пиши Админу в лс\n5.Для получения роли(лиги) нужно быть активным)\n\n\n         Роли       \n\n\nАдмин: Имеет все права.\nМодер: Имеет половину прав Админа.\nПремиум: у премиума больше шансов бить услышаним.У премиума есть доступ к прем чату и вип чату,минимальная лиги мастерская .\nVIP:у вип больше шансов бить услышаним,доступ к вип чату и минимальная лиги мастерская\nолд: уважение со стороны администрации,доступ к олд чату и военная лига\n (Геймер/Киберкотлета/CSер/Всадник Апокалипсиса/Fortniteр):роль на выбор не имеет приватных чатов и особых разрешений лига военная\n\n надеюсь эта информация была тебе полезной)\n Удачи!```""")
	embed=discord.Embed(title="Правила Сервера",colour = discord.Colour.green())
	embed.add_field(name="Знай их!",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def info(ctx):
	retStr = str("""```Информация о сервере:\n\n\nНазвание: natus est occidere\nСоздатель:ⓃⒶⒺⓄˣ𝓭𝓮₣𝟙𝓷𝓮\nАдминистрация:ⓃⒶⒺⓄˣBeRtot1R1US;ⓃⒶⒺⓄˣdog1e;\nМодерация:ⓃⒶⒺⓄˣMixer;ⓃⒶⒺⓄˣpØℝṧhє\nBOT:NAEO BOT\nСписок команд:!list\nКомандный префикс:!\nправила:!rule\nПомощь:!help```""")
	embed=discord.Embed(title="Информация",colour = discord.Colour.blue())
	embed.add_field(name="Info",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def information(ctx):
	retStr = str(f"""```Server Information:\n\n\nName: {ctx.guild}\nCreator:ⓃⒶⒺⓄˣ𝓭𝓮₣𝟙𝓷𝓮\nAdministration:ⓃⒶⒺⓄˣBeRtot1R1US;ⓃⒶⒺⓄˣdog1e;\nModerators:ⓃⒶⒺⓄˣMixer;ⓃⒶⒺⓄˣpØℝṧhє\nBOT:NAEO BOT\nCommand list:!command\nCommand prefix:!\nRules:!rules\nHelp:!help```""")
	embed=discord.Embed(title="info",colour = discord.Colour.blue())
	embed.add_field(name="Info",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def шутка(ctx):
	await ctx.send(random.choice(shutki))
@bot.command(pass_context=True)
async def talk(ctx):
	await ctx.send(random.choice(en))
@bot.command(pass_context=True)
async def list(ctx):
	retStr = str("""```css\n1.!bun бааан\n2.!help помощь\n3.!shytka рандомная шутка\n4.!банан определение банана\n5.!pogovori Я поговорю с тобой\n6.!rule правила сервера\n7.!info информация о сервере```""")
	embed=discord.Embed(title="List",colour = discord.Colour.green())
	embed.add_field(name="Команды",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def command(ctx):
	retStr = str("""```css\n1.!bunned buuuuun\n2.!help help\n3.!talk I'll talk to you\n4.!rules server rules\n5.!information server information```""")
	embed=discord.Embed(title="commands",colour = discord.Colour.green())
	embed.add_field(name="Commands",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def bunned(ctx):
	retStr = str("""```excel\n\n\nBBBBBBBBBBUUUUUUUUUUUUNNNNNNNNNNN```""")
	embed=discord.Embed(title="BUN",colour = discord.Colour.red())
	embed.add_field(name="BUN",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def rules(ctx):
	retStr = ("""```Hello! \nWell, let's see the rules \n \n \n1.There should not be bad words on the server that I will look for if you find a way to write you will be muddied by moderators or administrators) \n2. Only the Administration and moderators can use the nickname prefix ⓃⒶⒺⓄ\n3 .It is also not advisable to offend others \n4.Somebody have no right to mute you!\n5.To get a role (league) you need to be active)\n\n\n         Roles       \n\n\nAdmin: Has all rights.\nModer: Has half the rights of the Admin.\nPremium: premium has more chances to beat heard. Premium has access to prem chat and VIP chat.\nVIP: VIP has more chances to beat heard, access to VIP chat\nold: respect from the administration, access to old chat and military league\n (Gamer / Cyberkotlet / CSer / Horseman of the Apocalypse / Fortniter): the role of the choice does not have private chats and special permissions of the military league\n\n I hope this information was useful to you)\n Good luck```""")
	embed=discord.Embed(title="Server Rules",colour = discord.Colour.green())
	embed.add_field(name="Know them!",value=retStr)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def стих(ctx):
	retStr = (random.choice(stihi))
	embed=discord.Embed(title="Стих",colour = discord.Colour.orange())
	embed.add_field(name="ну посмотрим",value=retStr)
	await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def команды(ctx):
    retStr =  ("""```\nДа ладно Админ просит помощи у простого смертного!Ну ладно вот список команд:\n1.!user_mute @user мут пользователя на 60 секунд.\n2.!команды список команд\n3.!очистить очищает 1000 последних сообщений (если надо свое число то !очистить и нужное число команда тоже считается сообщением.)\n4.!Вип @user выдача вип пользователю\n5.!невип @user снять пользователя с вип\n6.!прем @user дать прем пользователю\n7.непрем @user забрать према\n8.!модер @user дать модера\n9.!немодер @user забрать модера\n10.!Ваня_работай добавить пользователя в чс сервера на 1 минуту\n```""")
    embed=discord.Embed(title="Админ команды",colour = discord.Colour.red())
    embed.add_field(name="не верю!",value=retStr)
    await ctx.author.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def очистить(ctx,amount = 1000):
    await ctx.channel.purge(limit = amount)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def Вип(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    vip_role = discord.utils.get(ctx.message.guild.roles,name = 'VIP')
    await member.add_roles(vip_role)
    retStr = (f"""```{member} получил VIP от администрации сервера!```""")
    embed=discord.Embed(title="Новый VIP",colour = discord.Colour.orange())
    embed.add_field(name="VIP",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def невип(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    vip_role = discord.utils.get(ctx.message.guild.roles,name = 'VIP')
    await member.remove_roles(vip_role)
    retStr = (f"""```{member} Был снят с роли VIP администрацией!```""")
    embed=discord.Embed(title="Сняли с VIP",colour = discord.Colour.orange())
    embed.add_field(name="VIP",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def прем(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    vip_role = discord.utils.get(ctx.message.guild.roles,name = 'премиум')
    await member.add_roles(vip_role)
    retStr = (f"""```{member} получил Премиум от администрации сервера!```""")
    embed=discord.Embed(title="Новый Премиум",colour = discord.Colour.green())
    embed.add_field(name="премиум",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def непрем(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    vip_role = discord.utils.get(ctx.message.guild.roles,name = 'премиум')
    await member.remove_roles(vip_role)
    retStr = (f"""```{member} Был снят с роли Премиум администрацией!```""")
    embed=discord.Embed(title="Сняли с премиум",colour = discord.Colour.green())
    embed.add_field(name="премиум",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def модер(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    mod_role = discord.utils.get(ctx.message.guild.roles,name = 'Модер')
    await member.add_roles(mod_role)
    retStr = (f"""```{member} получил Модератора от администрации сервера!```""")
    embed=discord.Embed(title="Новый Модератор",colour = discord.Colour.red())
    embed.add_field(name="Модератор",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def немодер(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    mod_role = discord.utils.get(ctx.message.guild.roles,name = 'Модер')
    await member.remove_roles(mod_role)
    retStr = (f"""```{member} Был снят с роли Модератора администрацией!```""")
    embed=discord.Embed(title="Сняли с Модератора",colour = discord.Colour.red())
    embed.add_field(name="Модератор",value=retStr)
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def user_mute(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    mute_role = discord.utils.get(ctx.message.guild.roles,name = 'mute')
    await member.add_roles(mute_role)
    await ctx.send(f'{member.mention} получил мут на пол часа за плохое поведение!')
    await asyncio.sleep(1800)
    unmute = discord.utils.get(ctx.message.guild.roles,name = 'mute')
    await member.remove_roles(unmute)
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def Ваня_работай(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    ch_role = discord.utils.get(ctx.message.guild.roles,name = 'ЧС')
    await member.add_roles(ch_role)
    await ctx.send(f'{member.mention} попал в ЧС на пол часа за плохое поведение!')
    await asyncio.sleep(1800)
    unch = discord.utils.get(ctx.message.guild.roles,name = 'ЧС')
    await member.remove_roles(unch)
class MyClient(discord.Client):
    async def on_ready(self):
        print('----------------------------------------\n\n\nLogged on as {0}!\n\n\n-----------------------------------------'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) # получаем объект канала
            message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
            try:
                emoji = str(payload.emoji) # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji])
                new = utils.get(message.guild.roles, id=config.new)
                newlg = utils.get(message.guild.roles, id=config.newlg)
                liga = utils.get(message.guild.roles, id=config.liga) # объект выбранной роли (если есть)
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.remove_roles(new)
                    await member.remove_roles(newlg)
                    await member.add_roles(role)
                    await member.add_roles(liga)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))

            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])
            new = utils.get(message.guild.roles, id=config.new)
            newlg = utils.get(message.guild.roles, id=config.newlg)
            liga = utils.get(message.guild.roles, id=config.liga)
            await member.remove_roles(role)
            await member.remove_roles(liga)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
emo = MyClient()
loop = asyncio.get_event_loop()
loop.create_task(emo.start(config.TOKEN))
loop.create_task(client.start(config.TOKEN))
loop.create_task(bot.start(config.TOKEN))
loop.run_forever()
