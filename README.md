# AI-Powered Blog Generator Using Llama-2 Model

## Abstract
This project is a Streamlit-based application that generates AI-powered blogs based on user input. Leveraging the Llama-2 model, it produces blogs tailored to specific audiences (researchers, data scientists, or common people) and generates content within a defined word limit. The model is implemented using LangChain's `CTransformers`, providing flexible control over the blog style, length, and topic. The project demonstrates the power of language models in content creation, offering a user-friendly interface for generating custom blog content in real-time.

## Key Features
- **Llama-2** based blog generation for different job profiles.
- Adjustable **word limit** and **blog style** selection.
- **Streamlit** interface for easy interaction.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dineshramv13/AI_BLOG_GENERATOR_USING_LLAMA2

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Download and place the Llama-2 model in the models/ directory.
4. Run the Streamlit app:
   ```bash
    streamlit run app.py

How It Works
Enter a topic for the blog.
Set the number of words for the blog.
Select the target blog style (e.g., Researchers, Data Scientists, Common People).
Click "Generate" to create the blog, which is generated using the Llama-2 model and displayed on the screen.
