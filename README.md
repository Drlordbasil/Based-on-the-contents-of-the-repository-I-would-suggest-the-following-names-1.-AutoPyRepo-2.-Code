# Autonomous Bot/AI Python Program for Ebook and Photo Generation

This Python project is a full autonomous bot/AI program that can generate ebooks and photos using different models and functions in combination with one another. The program utilizes the `openai` and `transformers` libraries to implement the functionality.

## Features

- Generate photo variations using the `openai.Image.create_variation` function.
- Chat with the AI assistant using the `openai.ChatCompletion.create` function.
- Load and chat with a pre-trained DialoGPT model using the `transformers` library.
- Generate and save ebooks compiled from chat conversations.

## Business Plan

The Autonomous Bot/AI Python Program for Ebook and Photo Generation has several potential business applications:

1. **Content Generation**: The program can be used to generate a variety of content, including ebooks and photos, for marketing, social media, or other creative purposes.

2. **Automated Customer Support**: The chatbot functionality can be utilized to create an automated customer support system, where customers can interact with the AI assistant to get information or assistance.

3. **Data Augmentation**: The photo generation capability can be used to augment existing datasets for image recognition or machine learning tasks, enabling the creation of more diverse and representative training data.

4. **Creative Writing Assistance**: The ebook generation feature can be useful for writers, helping them generate drafts or outline their ideas by conversing with the AI assistant.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3: https://www.python.org/downloads/
- `openai`: To install, run `pip install openai`.
- `transformers`: To install, run `pip install transformers`.
- Pre-trained models: The program utilizes the `microsoft/DialoGPT-medium` model, which will be automatically downloaded during program execution.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/autonomous-bot
   cd autonomous-bot
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace `image_path.jpg` with the path to your image file in the `main()` function of `autonomous_program.py`:

   ```python
   photo_generator = PhotoGenerator("<path_to_your_image_file>", "output_folder")
   ```

4. Run the program:

   ```bash
   python autonomous_program.py
   ```

## Usage

### Photo Generation

To generate variations of a photo, use the `run_photo_generation` method of the `AutonomousProgram` class. This method takes in two parameters: `n_variations` (the number of variations to generate) and `image_size` (the size of the variations).

Example usage:

```python
program = AutonomousProgram(chat_bot, photo_generator, ebook_generator)
program.run_photo_generation(n_variations=5, image_size="512x512")
```

### Ebook Generation

To generate an ebook from chat conversations, use the `run_ebook_generation` method of the `AutonomousProgram` class. This method generates an ebook text based on the provided chat history and saves it to a file.

Example usage:

```python
program = AutonomousProgram(chat_bot, photo_generator, ebook_generator)
program.run_ebook_generation()
```

### Chat Interaction

To interact with the chatbot and the DialoGPT model, use the `run_chat_interaction` method of the `AutonomousProgram` class. This method allows you to have a conversation with the chatbot.

Example usage:

```python
program = AutonomousProgram(chat_bot, photo_generator, ebook_generator)
program.run_chat_interaction(num_lines=3)
```

### Autonomous Program

To run the full autonomous program, which includes photo generation, ebook generation, and chat interaction, use the `run_autonomous_program` method of the `AutonomousProgram` class.

Example usage:

```python
program = AutonomousProgram(chat_bot, photo_generator, ebook_generator)
program.run_autonomous_program()
```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.