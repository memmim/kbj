import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):



    #비주 인사 대화

    if message.content == "비주야!" :
        await message.channel.send("저 여기 있어요!")
    
    if message.content == ("뭐야, 김비주. 또 길 잃었어?") :
         await message.channel.send("아니야! 나 여기 있었어. 우주형은 제 말 믿죠?")

    if message.content == ("...어? 당연히 믿지!") :
         await message.channel.send("...정말 너무해요.")



    #리혁 인사 대화

    if message.content == ("야!") :
        await message.channel.send("얘들아 싸우지 말자.")

    if message.content == ("풉") :
        await message.channel.send("우주형 그만 놀려.")



    #중현 인사 대화

    if message.content == ("까꿍") :
        await message.channel.send("김중현. 똑바로 인사해야지.")


    #지호 인사 대화

    if message.content == ("헐, 아니었어여? 맨날 화내는 줄.") :
        await message.channel.send("리혁아. 참자.")


    #우주 인사 대화

    if message.content == ("저도 사랑해요. 수플레.") :
        await message.channel.send("앗. 저도 많이 많이 사랑해요, 수플레!")



    ##불꽃놀이 트레일러 ver

    if message.content == ("멈출 수 없어") :
        await message.channel.send("NO way")

    if message.content == ("더는 망설이지마") :
        await message.channel.send("Alright")

    if message.content == ("어디 있는 걸까 넌") :
        await message.channel.send("Okay")

    if message.content == ("우리의 불꽃이야") :
        await message.channel.send("we shine so bright like a firework")

    if message.content == ("we shine so bright like a firework") :
        await message.channel.send("이 순간 온 세상에 보여주는 거야")

    if message.content == ("we shine so bright like a firework 이 순간 온 세상에 보여주는 거야") :
        await message.channel.send("화려했던 컬러")
    
    if message.content == ("화려했던 컬러") :
        await message.channel.send("너와 나의 색깔을 담아 colorful firework")