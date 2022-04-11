import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime
from datetime import datetime
import asyncio

from settings.config import *



class Recruit(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.form_reg = {}
        self.channel_id = int(CHANNEL_ID)
        self.server_id = int(SERVER_ID)
        self.app_body = app_body
        self.roles_id = roles_id
        self.guild_body = {}
        self._guilds_list = guilds_list
        self.questions = []
        self.guild:str = "guild name"
        return

    def set_guilds_menu(self):
        _guild_options:list = []

        for guild in self._guilds_list :
            _guild_option = it.SelectOption(label=guild,value=guild)#, emoji=it.Emoji(id=880221520121700362,animated=False)),
            _guild_options.append(_guild_option)

        _guilds_menu = it.SelectMenu(
                                    options= _guild_options,
                                    placeholder="Choose a Guild to Apply to",
                                    custom_id="chosen_guild",
                                )
        return _guilds_menu

    def set_form(self):
        _inputs = []
        if self.guild is not None and self.guild in self.app_body: #registered guild
            self.questions = self.app_body[self.guild]["questions"]
            _answers_placeholder = self.app_body[self.guild]["asnwers_placeholders"]
            _answers_length = self.app_body[self.guild]["answers_length"]
            for order in range(len(self.app_body[self.guild]["questions"])):
                question = TextInput(
                                style=TextStyleType.PARAGRAPH,
                                label=self.questions[order],
                                placeholder=_answers_placeholder[order],
                                min_length=_answers_length[order][0],
                                max_length=_answers_length[order][1],
                                required=True,
                                custom_id=f"question_{order}",
                                )
                _inputs.append(question)
        else: #non-registered guild (set to default)
            self.questions = self.app_body["Default"]["questions"]
            _answers_placeholder = self.app_body["Default"]["asnwers_placeholders"]
            _answers_length = self.app_body["Default"]["answers_length"]
            for order in range(len(self.questions)):
                question = TextInput(
                                    style=TextStyleType.PARAGRAPH,
                                    label=f"{self.questions[order]} {self.guild} ?" if order == 1 else f"{self.questions[order]}",
                                    placeholder=_answers_placeholder[order],
                                    min_length=_answers_length[order][0],
                                    max_length=_answers_length[order][1],
                                    required=True,
                                    custom_id=f"question_{order}",
                                    )
                _inputs.append(question)

        form_modal = Modal(
                            custom_id="app_form",
                            title=f"{self.guild} Guild Recruitment Form",
                            components=_inputs
                            )

        return form_modal

    def get_form(self,user:it.Member.user,answers):
        _fields = []
        if self.guild is not None and self.guild in self.app_body: #registered guild
            for _order in range(len(answers)):
                _field = it.EmbedField(
                                        name=f"{_order+1} - {self.questions[_order]}",
                                        value=f"{answers[_order]}"
                                        )
                _fields.append(_field)
        else: #non-registered guild (set to default)
            for _order in range(len(answers)):
                _field = it.EmbedField(
                                        name=f"{_order+1} - {self.questions[_order]} {self.guild} ?" if _order == 1 else f"{_order+1} - {self.questions[_order]}" ,
                                        value=f"{answers[_order]}"
                                        )
                _fields.append(_field)

        avatar_url = f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png"
        app_embed = it.Embed(
                            title=f"{self.guild} Guild Application",
                            color=0x00ff00,
                            fields=_fields,
                            timestamp=str(datetime.utcnow()),
                            author=it.EmbedAuthor(  
                                                name=f"{user.username}#{user.discriminator}",
                                                icon_url=avatar_url,
                                                )
                            )
        #app_embed.set_footer(f"Id : {user.id}")
        return app_embed

    @interactions.extension_command(
                name="join_guild",
                description="Fill a Recruitment Form And Send It To Guilds Leaders",
                scope=int(SERVER_ID)
                )        
    async def join_guild(self,ctx:CC):
        await ctx.defer()
        _menu = self.set_guilds_menu()
        await ctx.send("Apply Now !",components=_menu)
        await asyncio.sleep(15)
        await ctx.edit("timed out",components=[])

    @interactions.extension_component("chosen_guild")
    async def _chosen_guild(self,ctx,blah):
        self.guild = ctx.data.values[0]
        await ctx.popup(self.set_form())

    @interactions.extension_modal("app_form")
    async def app_response(self,ctx:CPC,*args):
        channel = it.Channel(**await self.bot._http.get_channel(self.channel_id), _client=self.bot._http)
        app_embed = self.get_form(ctx.member.user,args)
        await channel.send(f"application received\n<@&{roles_id[self.guild]}>",embeds=app_embed)#pings guild leaders for new apps
        await ctx.send("application submitted",components=[])


def setup(client : Client):
    Recruit(client)