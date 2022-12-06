import discord
from discord.ext import commands
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


class Summarizer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = 'summarize', description = '🤏 quickly shorten a text.')
    async def summarize(self, ctx, text: discord.Option(str)):
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        
        freqTable = dict()

        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues / len(sentenceValue))
        
        summary = ''

        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence

        total_len  = len(text)
        summary_len = len(summary)
        percent_len = round(summary_len/total_len*100, 2)

        embed = discord.Embed(title = 'summarizer.exe', description = f'```yaml\n{summary}\n```')
        embed.set_footer(text='💡 Click on your command to see the input text!')
        await ctx.send(f'Your text is now about {percent_len}% shorter ✔️')
        await ctx.respond(embed=embed)
        print(summary)


def setup(bot):
    bot.add_cog(Summarizer(bot))
