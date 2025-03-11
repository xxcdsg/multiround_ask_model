from openai import OpenAI

def ask_one(api_key,key_word,word,selected_model) :

    if selected_model.count("deepseek"):

        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": key_word},
                {"role": "user", "content": word},
            ],
            temperature=0.7,
            stream=False
        )

        return response.choices[0].message.content