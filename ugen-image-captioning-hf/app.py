import gradio as gr
from uform import gen_model
from PIL import Image
import torch

# Load the model and processor
model = gen_model.VLMForCausalLM.from_pretrained("unum-cloud/uform-gen")
processor = gen_model.VLMProcessor.from_pretrained("unum-cloud/uform-gen")

def gradio_ask_multiple_images(images, prompt):
    accumulated_text=""
    for image in images:
        image = Image.open(image).convert("RGB")
        # Process the image and the prompt
        inputs = processor(texts=[prompt], images=[image], return_tensors="pt")

        # Generate the output
        with torch.inference_mode():
            output = model.generate(
                **inputs,
                do_sample=False,
                use_cache=True,
                max_new_tokens=128,
                eos_token_id=32001,
                pad_token_id=processor.tokenizer.pad_token_id
            )

        prompt_len = inputs["input_ids"].shape[1]
        decoded_text = processor.batch_decode(output[:, prompt_len:])[0]
        print(decoded_text)
        accumulated_text += f"Image name: {image}, chatbot reply: {decoded_text}\n"
    with open("textfromUgen.txt", "w") as text_file:
        text_file.write(accumulated_text)

    return accumulated_text

# Define the Gradio interface
description = """ugen to caption image"""

def gradio_interface(images, user_message):
    all_text_outputs = gradio_ask_multiple_images(images, user_message)
    return all_text_outputs


# UI for uploading images @Malik
with gr.Blocks() as demo:
    with gr.Row():
        image_input = gr.File(label="Upload multiple images", file_count="multiple" , type="filepath")
        user_message_input = gr.Textbox(label="Enter your message")
        temperature_input = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5, label="Temperature")
    submit_button = gr.Button("Submit")
    output_text = gr.Textbox(label="Output")

    # Link the interface with the processing function
    submit_button.click(
        fn=gradio_interface,
        inputs=[image_input, user_message_input],
        outputs=output_text
    )

demo.launch(share=True)
