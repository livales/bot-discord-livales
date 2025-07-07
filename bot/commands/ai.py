import discord
import openai
from bot.config import LIVALES_CONTEXT, WEBSITE_URL
from bot.utils.embeds import create_embed

def setup(bot):
    @bot.slash_command(name="ask", description="Tanyakan apa saja kepada Livales Bot")
    async def ask(ctx, pertanyaan: str):
        """Menjawab pertanyaan menggunakan ChatGPT API."""
        # Defer response karena API call mungkin memakan waktu
        await ctx.defer()
        
        try:
            # Panggil OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": LIVALES_CONTEXT + f"\nSelalu sertakan link website {WEBSITE_URL} dalam jawaban jika relevan."},
                    {"role": "user", "content": pertanyaan}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            answer = response.choices[0].message.content
            
            # Buat embed untuk response
            embed = create_embed(
                title="🤖 Livales Bot Menjawab",
                color=discord.Color.purple()
            )
            embed.add_field(name="❓ Pertanyaan", value=pertanyaan[:256], inline=False)
            embed.add_field(name="💬 Jawaban", value=answer[:1024], inline=False)
            
            # Tambahkan link website jika tidak ada dalam jawaban
            if "livales.netlify.app" not in answer.lower():
                embed.add_field(
                    name="🌐 Info Lebih Lanjut",
                    value=f"[Kunjungi Website Livales]({WEBSITE_URL})",
                    inline=False
                )
            
            embed.set_footer(text="Powered by OpenAI GPT-3.5 | Livales Bot")
            
            await ctx.followup.send(embed=embed)
            
        except Exception as e:
            error_embed = create_embed(
                title="❌ Error",
                description=f"Maaf, terjadi kesalahan saat memproses pertanyaan Anda.",
                color=discord.Color.red()
            )
            error_embed.add_field(
                name="💡 Saran",
                value="Coba lagi nanti atau hubungi admin server.",
                inline=False
            )
            await ctx.followup.send(embed=error_embed, ephemeral=True)