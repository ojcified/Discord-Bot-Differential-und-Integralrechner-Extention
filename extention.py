import requests
import json
import urllib.parse

WOLF = os.getenv('WAID') # importiert den Token für Wolframalpha aus einer .env

@client.command(pass_context=True)
async def diff(ctx, useri):
    diffback = ["Ergebnisse:"]
    await ctx.message.author.send("Eingabe:# "+useri+" #")
        input = urllib.parse.quote(useri)
        if ctx.channel.type == discord.ChannelType.private:
            url="http://api.wolframalpha.com/v2/query?input="+input+'&appid='+WOLF+"&includepodid=Partial%20derivatives&includepodid=Derivative&output=json"
            response = requests.get(url)
            if 'Derivative' in response.text or 'Partial derivatives' in response.text:
                query = json.loads(response.text)
                for x in query["queryresult"]["pods"]:
                    for y in x["subpods"]:
                        diffback.append(y["plaintext"])
                await ctx.message.author.send('\n'.join(diffback))
            else:
                await ctx.message.author.send('###################\n Keine Ableitung gefunden! \n###################\n  Bitte Syntax überprüfen!\n###################\n')

@client.command(pass_context=True)
async def inin(ctx, useri):
    ininback = ["Ergebnisse:"]
    await ctx.message.author.send("Eingabe:# "+useri+" #")
        input = urllib.parse.quote(useri)
        if ctx.channel.type == discord.ChannelType.private:
            url="http://api.wolframalpha.com/v2/query?input="+input+'&appid='+WOLF+"&includepodid=Indefinite%20integral&output=json"
            response = requests.get(url)
            if 'Indefinite integral' in response.text:
                query = json.loads(response.text)
                for x in query["queryresult"]["pods"]:
                    for y in x["subpods"]:
                        ininback.append(y["plaintext"])
                await ctx.message.author.send('\n'.join(ininback))
            else:
                await ctx.message.author.send('###################\n Kein Integral gefunden! \n###################\n  Bitte Syntax überprüfen!\n###################\n')
