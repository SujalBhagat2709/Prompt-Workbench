from template_manager import TemplateManager
from prompt_builder import PromptBuilder
from history_manager import HistoryManager


class PromptWorkbench:

    def __init__(self):

        self.template_manager = TemplateManager()

        self.prompt_builder = PromptBuilder()

        self.history_manager = HistoryManager()

    def generate_prompt(self):

        print("\n========== GENERATE PROMPT ==========\n")

        self.template_manager.show_templates()

        try:

            template_id = int(

                input(

                    "\nChoose Template: "

                )

            )

        except:

            print("\nInvalid Choice")

            return

        selected = self.template_manager.get_template(

            template_id

        )

        if selected is None:

            print("\nTemplate Not Found")

            return

        print("\nEnter Prompt Details\n")

        task = input("Task: ")

        tone = input("Tone: ")

        audience = input("Audience: ")

        length = input("Length: ")

        keywords = input("Keywords (comma separated): ")

        final_prompt = self.prompt_builder.build_prompt(

            selected["template"],

            task,

            tone,

            audience,

            length,

            keywords

        )

        print("\n==============================")

        print("GENERATED PROMPT")

        print("==============================\n")

        print(final_prompt)

        file_name = self.prompt_builder.save_prompt(

            final_prompt

        )

        self.history_manager.add_prompt(

            selected["name"],

            task,

            final_prompt

        )

        print(

            f"\nPrompt Saved To: {file_name}"

        )

    def view_history(self):

        self.history_manager.show_history()

    def search_history(self):

        keyword = input(

            "\nSearch Keyword: "

        )

        self.history_manager.search_prompt(

            keyword

        )

    def clear_history(self):

        answer = input(

            "\nClear all history? (y/n): "

        )

        if answer.lower() == "y":

            self.history_manager.delete_history()

    def menu(self):

        while True:

            print("\n")

            print("=" * 35)

            print("      PROMPT WORKBENCH")

            print("=" * 35)

            print("1. Generate Prompt")

            print("2. View History")

            print("3. Search Prompt")

            print("4. Clear History")

            print("5. Exit")

            choice = input(

                "\nEnter Choice: "

            )

            if choice == "1":

                self.generate_prompt()

            elif choice == "2":

                self.view_history()

            elif choice == "3":

                self.search_history()

            elif choice == "4":

                self.clear_history()

            elif choice == "5":

                print(

                    "\nThank You!"

                )

                break

            else:

                print(

                    "\nInvalid Choice"

                )


if __name__ == "__main__":

    app = PromptWorkbench()

    app.menu()