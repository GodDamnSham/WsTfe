# Wordspace for TFE

This repository contains updated models, scripts, and the sentences we used for sentiment analysis, keyword analysis, and semantic search.

## Scripts

to run the scripts open the file in VS code run it on the mentioned python env. 


## Models

In this section, the commands to run the models are mentioned. After running the commands, open the Gradio link that appears, select multiple pictures, add a prompt in the text box, and click **Submit**.

> **Note:** In case of any updates to Python libraries, the requirements file needs to be updated accordingly.

    ```bash
    # Update the requirements file
    pip freeze > requirements.txt
    ```

## Run miniGpt on Google Colab

- **Use the format:** (number_Image_imagename)
    - **Example:** `1_Image_testimage.png`
    
    ```bash
    %cd /Path/miniGpt-v2
    !pip install -r requirements.txt
    !python myimp.py
    ```

## Run miniGpt Locally

- **Use the format:** (number_Image_imagename)
    - **Example:** `1_Image_testimage.png`

    ```bash
    cd /Path/miniGpt-v2
    pip install -r requirements.txt
    python myimp.py
    ```

## Run InstructBlip on Google Colab

    ```bash
    %cd /Path/InstructBlipImplementation
    !pip install -r requirements.txt
    !python instructBlip.py
    ```

## Run InstructBlip Locally

    ```bash
    cd /Path/InstructBlipImplementation
    pip install -r requirements.txt
    python instructBlip.py
    ```

## Run UForm-Gen on Google Colab

    ```bash
    %cd /Path/ugen-image-captioning-hf
    !pip install -r requirements.txt
    !python app.py
    ```

## Run UForm-Gen Locally

    ```bash
    cd /Path/ugen-image-captioning-hf
    pip install -r requirements.txt
    python app.py
    ```


