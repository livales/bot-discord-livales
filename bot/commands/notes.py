import discord
from datetime import datetime
from bot.utils.storage import user_notes
from bot.utils.embeds import create_embed

def setup(bot):
    @bot.slash_command(name="take-note", description="Simpan catatan pribadi Anda")
    async def take_note(ctx, catatan: str):
        """Menyimpan catatan dari pengguna."""
        user_id = str(ctx.author.id)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Inisialisasi list catatan untuk user jika belum ada
        if user_id not in user_notes:
            user_notes[user_id] = []
        
        # Simpan catatan
        note_data = {
            "timestamp": timestamp,
            "note": catatan
        }
        user_notes[user_id].append(note_data)
        
        # Buat embed untuk response
        embed = create_embed(
            title="📝 Catatan Tersimpan!",
            description=f"Catatan Anda telah berhasil disimpan.",
            color=discord.Color.green()
        )
        embed.add_field(name="⏰ Waktu", value=timestamp, inline=False)
        embed.add_field(name="📄 Catatan", value=catatan[:1024], inline=False)
        embed.set_footer(text=f"Total catatan Anda: {len(user_notes[user_id])}")
        
        await ctx.respond(embed=embed, ephemeral=True)

    @bot.slash_command(name="my-notes", description="Lihat semua catatan Anda")
    async def my_notes(ctx):
        """Menampilkan semua catatan pengguna."""
        user_id = str(ctx.author.id)
        
        if user_id not in user_notes or len(user_notes[user_id]) == 0:
            # Lanjutan bot/commands/notes.py
            embed = create_embed(
                title="📭 Tidak Ada Catatan",
                description="Anda belum memiliki catatan tersimpan.",
                color=discord.Color.yellow()
            )
            embed.add_field(
                name="💡 Tips",
                value="Gunakan `/take-note [catatan]` untuk membuat catatan baru!",
                inline=False
            )
            await ctx.respond(embed=embed, ephemeral=True)
            return
        
        # Buat embed untuk menampilkan catatan
        embed = create_embed(
            title="📚 Catatan Anda",
            description=f"Total: {len(user_notes[user_id])} catatan tersimpan",
            color=discord.Color.blue()
        )
        
        # Tampilkan maksimal 5 catatan terakhir
        for note in user_notes[user_id][-5:]:
            embed.add_field(
                name=f"📅 {note['timestamp']}",
                value=note['note'][:256] + "..." if len(note['note']) > 256 else note['note'],
                inline=False
            )
        
        if len(user_notes[user_id]) > 5:
            embed.set_footer(text="📌 Menampilkan 5 catatan terakhir")
        
        await ctx.respond(embed=embed, ephemeral=True)

    @bot.slash_command(name="clear-notes", description="Hapus semua catatan Anda")
    async def clear_notes(ctx):
        """Menghapus semua catatan pengguna."""
        user_id = str(ctx.author.id)
        
        if user_id in user_notes and len(user_notes[user_id]) > 0:
            count = len(user_notes[user_id])
            
            # Buat embed konfirmasi
            confirm_embed = create_embed(
                title="⚠️ Konfirmasi Penghapusan",
                description=f"Anda akan menghapus **{count} catatan**. Tindakan ini tidak dapat dibatalkan!",
                color=discord.Color.orange()
            )
            
            # Buat view dengan tombol konfirmasi
            class ConfirmView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=30)
                    self.value = None
                
                @discord.ui.button(label="✅ Ya, Hapus", style=discord.ButtonStyle.danger)
                async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
                    if interaction.user.id == ctx.author.id:
                        user_notes[user_id] = []
                        
                        success_embed = create_embed(
                            title="🗑️ Catatan Dihapus",
                            description=f"Berhasil menghapus {count} catatan.",
                            color=discord.Color.green()
                        )
                        await interaction.response.edit_message(embed=success_embed, view=None)
                        self.value = True
                        self.stop()
                    else:
                        await interaction.response.send_message("Anda tidak dapat menggunakan tombol ini.", ephemeral=True)
                
                @discord.ui.button(label="❌ Batal", style=discord.ButtonStyle.secondary)
                async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
                    if interaction.user.id == ctx.author.id:
                        cancel_embed = create_embed(
                            title="✅ Dibatalkan",
                            description="Penghapusan catatan dibatalkan.",
                            color=discord.Color.blue()
                        )
                        await interaction.response.edit_message(embed=cancel_embed, view=None)
                        self.value = False
                        self.stop()
                    else:
                        await interaction.response.send_message("Anda tidak dapat menggunakan tombol ini.", ephemeral=True)
            
            view = ConfirmView()
            await ctx.respond(embed=confirm_embed, view=view, ephemeral=True)
            
        else:
            empty_embed = create_embed(
                title="📭 Tidak Ada Catatan",
                description="Anda tidak memiliki catatan untuk dihapus.",
                color=discord.Color.yellow()
            )
            await ctx.respond(embed=empty_embed, ephemeral=True)