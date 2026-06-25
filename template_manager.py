class TemplateManager:

    def __init__(self):

        self.templates = {

            1: {

                "name": "LinkedIn Post",

                "template":

"""Write a {length} LinkedIn post.

Tone:
{tone}

Audience:
{audience}

Keywords:
{keywords}

Task:
{task}
"""

            },

            2: {

                "name": "Professional Email",

                "template":

"""Write a {tone} email.

Audience:
{audience}

Purpose:
{task}

Include:

{keywords}
"""

            },

            3: {

                "name": "Resume",

                "template":

"""Create a professional resume.

Target Role:
{task}

Skills:

{keywords}

Tone:

{tone}
"""

            },

            4: {

                "name": "YouTube Script",

                "template":

"""Create a {length} YouTube script.

Topic:

{task}

Audience:

{audience}

Keywords:

{keywords}

Tone:

{tone}
"""

            },

            5: {

                "name": "Blog Post",

                "template":

"""Write a {length} blog.

Topic:

{task}

Audience:

{audience}

Keywords:

{keywords}

Tone:

{tone}
"""

            }

        }

    def show_templates(self):

        print("\nAvailable Templates\n")

        for key, value in self.templates.items():

            print(

                f"{key}. {value['name']}"

            )

    def get_template(

        self,

        template_id

    ):

        return self.templates.get(

            template_id

        )