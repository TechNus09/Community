import os
"""the channel id where the applications will be sent"""
CHANNEL_ID = 960586298710708284

"""the server id"""
SERVER_ID = os.getenv("SERVER_ID")

"""the bot token saved in env vars as 'TOKEN' """
TOKEN = os.getenv("TOKEN")

"""guilds applications' bodies"""
roles_id =  {"Default": 999999999999999999,
            "OwO": 962617518156029952,
            "PHG": 962617427055738960,
            "LAT": 962617556378722335,
            "FALL": 962617490985328690,
            "MR": 962617593305391145,
            "NX": 962617640445161472,
            "TWH": 962617672279941171,
            "AoE": 962617708904591410,
            "TGR": 963843439148032000
            }

guilds_list=[
            "OwO",
            "PHG",
            "LAT",
            "FALL",
            "MR",
            "NX",
            "TWH",
            "AoE",
            "TGR"
            ]
app_body={
        "Default":{
                    "leader_role":roles_id["Default"],
                    "questions":[
                                "What is your ingame-name",
                                "Why do you want to join",#+guild tag+" ?"
                                "How often do you play Curse of Aros?"
                                    ],
                    "questions_tags":[
                                "",
                                "",
                                ""
                                ],
                    "answers_length":[
                                    [3 ,14 ],
                                    [3 ,2000 ],
                                    [2 ,50 ]
                                    ],
                    "asnwers_placeholders":[
                                            "Answer here ...",
                                            "Explain here ...",
                                            "Answer here ..."
                                            ],
                    "guild_icon":"emoji_code"
                    },
        "NX" :  {
                "leader_role":roles_id["NX"],
                "questions":[
                            "What's your ingame name:",
                            "Current Gear:",
                            "Are you above 17yrs old:",
                            "What's your goal ingame in terms of gear/exp:",
                            "What you look for in a guild:"
                            ],
                "questions_tags":[
                            "",
                            "",
                            "",
                            "",
                            ""
                            ],
                "answers_length":[
                                [3 ,14 ],
                                [10 ,300 ],
                                [2 ,3 ],
                                [3 ,2000 ],
                                [3 ,2000 ],
                                ],
                "asnwers_placeholders":[
                                        "Answer here ...",
                                        "Answer here ...",
                                        "(Yes/No)",
                                        "Answer here ...",
                                        "Answer here ..."
                                        ],
                "guild_icon":"emoji_code"
                },
        "OwO" : {
                "leader_role":roles_id["OwO"],
                "questions":[
                            "why do you think you will fit well into OwO:",
                            "Homeworld is W4. Can you play mainly in W4:",
                            "Explain your sense of humour:",
                            "Would you help a low level player in need:",
                            "Explain your answer for question #4:"
                            ],
                "questions_tags":[
                                "",
                                "",
                                "",
                                "",
                                ""
                            ],
                "answers_length":[
                                [3 ,2000 ],
                                [3 ,1000 ],
                                [3 ,2000 ],
                                [2 ,3 ],
                                [3 ,2000 ],
                                ],
                "asnwers_placeholders":[
                                        "Explain here ...",
                                        "(Yes | No [explain why no])",
                                        "Explain here ...",
                                        "(Yes/No)",
                                        "Explain here ..."],
                "guild_icon":"emoji_code"
                },
        "AoE":{
                "leader_role":roles_id["AoE"],
                "questions":[
                            "What's your ingame name?",
                            "What are your combat/skills levels?",
                            "Were you in a guild previously?(if yes:name)",
                            "How long have you played CoA?",
                            "Are you active in both CoA and discord?"
                            ],
                "questions_tags":[
                                "",
                                "",
                                "",
                                "",
                                ""
                                ],
                "answers_length":[
                                [3 ,14 ],
                                [20,1000],
                                [2,1000],
                                [3,1000]
                                [3,1000]
                                ],
                "asnwers_placeholders":[
                                        "Answer here ...",
                                        "Answer here ...",
                                        "(Yes [guild name] | No)"
                                        "Answer here ...",
                                        "Answer here ..."
                                       ],
                "guild_icon":"emoji_code"
                    },
        "TGR":{
                "leader_role":roles_id["TRG"],
                "questions":[
                            "What's your ingame name?",
                            "How long have you played MMO's?",
                            "How long have you played CoA?",
                            "Why do you want to join TGR?",
                            "How can we help?"
                            ],
                "questions_tags":[
                                "",
                                "",
                                "",
                                "",
                                ""
                                ],
                "answers_length":[
                                [3,14],
                                [3,1000],
                                [3,1000],
                                [3,2000],
                                [3,2000]
                                ]
                "asnwers_placeholders":[
                                        "Answer here ...",
                                        "Answer here ...",
                                        "Answer here ...",
                                        "Explain here ...",
                                        "Explain here ..."
                                        ],
                "guild_icon":"emoji_code"
                }
        
        }
