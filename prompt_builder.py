from datetime import datetime


class PromptBuilder:

    def __init__(self):

        pass

    def build_prompt(

        self,

        template,

        task,

        tone,

        audience,

        length,

        keywords

    ):

        prompt = template.format(

            task=task,

            tone=tone,

            audience=audience,

            length=length,

            keywords=keywords

        )

        return prompt

    def save_prompt(

        self,

        prompt

    ):

        file_name = (

            "generated_prompt.txt"

        )

        with open(

            file_name,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "PROMPT WORKBENCH\n"

            )

            file.write(

                "=" * 40

            )

            file.write(

                "\n\n"

            )

            file.write(prompt)

            file.write(

                "\n\n"

            )

            file.write(

                "=" * 40

            )

            file.write(

                "\nGenerated On: "

            )

            file.write(

                datetime.now()

                .strftime(

                    "%d-%m-%Y %H:%M:%S"

                )

            )

        return file_name