import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime
from datetime import datetime
import config
from config import CHANNEL_ID
from config import SERVER_ID


class Recruit(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.form_reg = {}
        self.channel_id = CHANNEL_ID
        self.server_id = SERVER_ID
        return
    

    def set_form(self):
        form_modal = Modal(
        custom_id="app_form",
        title="Guild Recruitment Form",
        components=[
                    TextInput(
                        style=TextStyleType.SHORT,
                        label="What Guild You're Interested In?",
                        placeholder="Enter Guild Tag",
                        min_length=2,
                        max_length=10,
                        required=True,
                        custom_id="guild_tag",
                    ),
                    TextInput(
                        style=TextStyleType.SHORT,
                        label="Please Enter Your Ingame Name : ",
                        placeholder="Your ingame-name",
                        min_length=3,
                        max_length=14,
                        required=True,
                        custom_id="ingame_name",
                    ),
                    TextInput(
                        style=TextStyleType.PARAGRAPH,
                        label="Why Do You Wanna Join This Guild?",
                        placeholder="State Your Reason here ...",
                        min_length=3,
                        max_length=2000,
                        required=True,
                        custom_id="join_reason",
                    ),
                    TextInput(
                        style=TextStyleType.PARAGRAPH,
                        label="How Ofen Do You Play Curse Of Aros?",
                        placeholder="Answer here ...",
                        min_length=3,
                        max_length=500,
                        required=True,
                        custom_id="play_freq",
                    ),
                ],
            )

        return form_modal



    def get_form(self,guild_tag:str,user:it.Member.user,ign:str,reason:str,play_rate:str):
        fields=[
                it.EmbedField(  
                name="1 - Which Guild You Are Applying to ?",
                value=f"{guild_tag.upper()} Guild"
                ),
                it.EmbedField(  
                name="2 - What Is Your ingame-name ?",
                value=ign
                ),
                it.EmbedField(  
                name=f"3 - Why Do You Want To Join {guild_tag.upper()} ?",
                value=reason
                ),
                it.EmbedField(  
                name="4 - How Often Do You Play Curse of Aros?",
                value=play_rate
                ),
                ]
        avatar_url = f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png"
        app_embed = it.Embed(
                            title=f"{guild_tag.upper()}' Guild Application",
                            color=0x00ff00,
                            fields=fields,
                            timestamp=str(datetime.utcnow()),
                            author=it.EmbedAuthor(  
                                                name=f"{user.username}#{user.discriminator}",
                                                icon_url=avatar_url,
                                                )
                            )
        app_embed.set_footer(f"Id : {user.id}")
        return app_embed

    @interactions.extension_command(
                name="join_guild",
                description="Fill a Recruitment Form And Send It To Guilds Leaders",
                scope=int(SERVER_ID)
                )        
    async def join_guild(self,ctx:CC):
        await ctx.popup(self.set_form())

    @interactions.extension_modal("app_form")
    async def app_response(self,ctx:CPC,guild_tag,ign,reason,playrate):
        channel = it.Channel(**await self.bot._http.get_channel(self.channel_id), _client=self.bot._http)
        app_embed = self.get_form(str(guild_tag),ctx.user,str(ign),str(reason),str(playrate))
        await channel.send("application received",embeds=app_embed)
        await ctx.send("application submitted")





def setup(client : Client):
    Recruit(client)