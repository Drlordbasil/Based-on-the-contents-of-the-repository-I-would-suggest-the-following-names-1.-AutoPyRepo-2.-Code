import openai
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from typing import List, Dict


class PhotoGenerator:
    def __init__(self, image_path: str, output_folder: str) -> None:
        self.image_path = image_path
        self.output_folder = output_folder

    def generate_variations(self, n: int, size: str) -> List[str]:
        response = openai.Image.create_variation(
            image=open(self.image_path, "rb"),
            n=n,
            size=size
        )
        image_urls = [image['url'] for image in response['data']]
        return image_urls


class EbookGenerator:
    def __init__(self, model: str) -> None:
        self.model = model

    def generate_ebook(self, chat_history: List[Dict[str, str]]) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=chat_history
        )
        assistant_response = response['choices'][0]['message']['content']
        return assistant_response

    def save_ebook(self, ebook_text: str, output_file: str) -> None:
        with open(output_file, 'w') as f:
            f.write(ebook_text)


class ChatBot:
    def __init__(self, model: AutoModelForCausalLM, tokenizer: AutoTokenizer) -> None:
        self.model = model
        self.tokenizer = tokenizer
        self.chat_history_ids = None

    def chat(self, num_lines: int) -> None:
        for step in range(num_lines):
            user_input = input(">> User:")

            new_user_input_ids = self.tokenizer.encode(
                user_input + self.tokenizer.eos_token, return_tensors='pt')
            bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids],
                                      dim=-1) if step > 0 else new_user_input_ids

            chat_history_ids = self.model.generate(bot_input_ids, max_length=1000,
                                                   pad_token_id=self.tokenizer.eos_token_id)

            bot_response = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0],
                                                 skip_special_tokens=True)
            print("DialoGPT: {}".format(bot_response))
            self.chat_history_ids = chat_history_ids


class AutonomousProgram:
    def __init__(self, chat_bot: ChatBot, photo_generator: PhotoGenerator, ebook_generator: EbookGenerator) -> None:
        self.photo_generator = photo_generator
        self.ebook_generator = ebook_generator
        self.chat_bot = chat_bot

    def run_photo_generation(self, n_variations: int, image_size: str) -> None:
        image_urls = self.photo_generator.generate_variations(
            n_variations, image_size)
        print("Generated variations:")
        for url in image_urls:
            print(url)

    def run_ebook_generation(self) -> None:
        chat_history = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
        ebook_text = self.ebook_generator.generate_ebook(chat_history)
        # Add timestamp to avoid overwriting previous ebooks
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = f"ebook_{timestamp}.txt"
        self.ebook_generator.save_ebook(ebook_text, output_file)
        print(f"Ebook '{output_file}' generated and saved successfully.")

    def run_chat_interaction(self, num_lines: int) -> None:
        self.chat_bot.chat(num_lines)

    def run_autonomous_program(self) -> None:
        self.run_photo_generation(1, "1024x1024")
        self.run_ebook_generation()
        self.run_chat_interaction(5)


def main() -> None:
    photo_generator = PhotoGenerator("image_path.jpg", "output_folder")
    ebook_generator = EbookGenerator("gpt-3.5-turbo")
    chat_bot = ChatBot(AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium"),
                       AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium"))
    program = AutonomousProgram(chat_bot, photo_generator, ebook_generator)
    program.run_autonomous_program()


if __name__ == '__main__':
    main()
