# Prompt Workbench

## Overview

Prompt Workbench is a terminal-based AI prompt generator that helps users create well-structured prompts for different use cases.

Users can:

- Generate prompts using predefined templates
- Save prompts
- View prompt history
- Search previous prompts
- Clear prompt history

---

## Features

- LinkedIn Post Template
- Professional Email Template
- Resume Template
- Blog Template
- YouTube Script Template
- Prompt History
- Prompt Search
- Export Prompt to TXT

---

## Project Structure

prompt-workbench/

├── template_manager.py

├── prompt_builder.py

├── history_manager.py

├── workbench.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.8+

No external libraries required.

---

## Run

```bash
python workbench.py
```

---

## Menu

```
1. Generate Prompt

2. View History

3. Search Prompt

4. Clear History

5. Exit
```

---

## Example

Choose Template

```
LinkedIn Post
```

Enter

```
Task

Tone

Audience

Length

Keywords
```

Generated

```
Write a medium LinkedIn post.

Tone:
Professional

Audience:
Recruiters

Keywords:
Python, AI

Task:
LinkedIn Post
```

---

## Generated Files

generated_prompt.txt

history.json

---

## Future Improvements

- AI API Integration
- OpenAI Support
- Gemini Support
- Ollama Support
- Custom Templates
- Export PDF
- Prompt Categories
- Prompt Rating
- Prompt Favorites

---

## Author

Developed using Python.