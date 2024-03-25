from transformers import InstructBlipProcessor, InstructBlipForConditionalGeneration
import torch
from PIL import Image
import requests
import gradio as gr
import re
import csv
import cv2

processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")
model = InstructBlipForConditionalGeneration.from_pretrained("Salesforce/instructblip-vicuna-7b"
, load_in_4bit=True, torch_dtype=torch.float16)





#@Malik
def gradio_ask_multiple_images(images, user_message,temperature_input):
    output=""
    csvdata = []
    for image in images:
#url = "https://raw.githubusercontent.com/salesforce/LAVIS/main/docs/_static/Confusing-Pictures.jpg"
        image = Image.open(image).convert("RGB")

# prepare image and prompt for the model
        prompt = user_message
        inputs = processor(images=image, text=prompt, return_tensors="pt").to(device="cuda", dtype=torch.float16)

# autoregressively generate an answer
        outputs = model.generate(
                 **inputs,
                do_sample=True,
                num_beams=10,
                max_new_tokens=512,
                min_length=16,
                top_p=0.9,
                repetition_penalty=1.5,
                #length_penalty=1.0,
                temperature=temperature_input,
                )
        number = re.search(r'/(\d+)_Image', image).group(1)
        generated_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
        output += f"image:{image} , output:{generated_text}\n"
        print(generated_text)
        csvdata.append(generated_text)

    with open("textfromBLip.txt", "w") as text_file:
        text_file.write(output)
      
    with open("llm_messages_csv.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["folder", "text"])  # Write header
        for cb in csvdata:
            writer.writerow(cb)
    return output


def gradio_interface(images, user_message,temperature_input):
    all_text_outputs = gradio_ask_multiple_images(images, user_message,temperature_input)
    return all_text_outputs


# UI for uploading images @Malik
with gr.Blocks() as demo:
    with gr.Row():
        image_input = gr.Files(label="Upload multiple images", file_count="multiple")
        user_message_input = gr.Textbox(label="Enter your message")
        temperature_input = gr.Slider(minimum=0, maximum=1, step=0.1, value=1, label="Temperature")
    submit_button = gr.Button("Submit")
    output_text = gr.Textbox(label="Output")

    # Link the interface with the processing function
    submit_button.click(
        fn=gradio_interface,
        inputs=[image_input, user_message_input,temperature_input],
        outputs=output_text
    )


demo.launch(share=True)
