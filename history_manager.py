import json
import os
from datetime import datetime


class HistoryManager:

    def __init__(self):

        self.history_file = "history.json"

        self.history = []

        self.load_history()

    def load_history(self):

        if os.path.exists(
            self.history_file
        ):

            try:

                with open(

                    self.history_file,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.history = json.load(
                        file
                    )

            except:

                self.history = []

    def save_history(self):

        with open(

            self.history_file,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.history,

                file,

                indent=4

            )

    def add_prompt(

        self,

        template,

        task,

        prompt

    ):

        self.history.append(

            {

                "date":

                datetime.now()

                .strftime(

                    "%d-%m-%Y %H:%M:%S"

                ),

                "template":

                template,

                "task":

                task,

                "prompt":

                prompt

            }

        )

        self.save_history()

    def show_history(self):

        if not self.history:

            print(

                "\nNo Prompt History."

            )

            return

        print(

            "\n========== HISTORY ==========\n"

        )

        for index, item in enumerate(

            self.history,

            start=1

        ):

            print(

                f"{index}. "

                f"{item['template']}"

            )

            print(

                f"Task : "

                f"{item['task']}"

            )

            print(

                f"Date : "

                f"{item['date']}"

            )

            print(

                "-" * 40

            )

    def search_prompt(

        self,

        keyword

    ):

        keyword = keyword.lower()

        found = False

        print()

        for item in self.history:

            if (

                keyword in item["task"].lower()

                or

                keyword in item["template"].lower()

                or

                keyword in item["prompt"].lower()

            ):

                found = True

                print(

                    item["date"]

                )

                print(

                    item["template"]

                )

                print(

                    item["task"]

                )

                print(

                    "-" * 40

                )

        if not found:

            print(

                "No Matching Prompt Found."

            )

    def delete_history(self):

        self.history.clear()

        self.save_history()

        print(

            "\nHistory Cleared."

        )