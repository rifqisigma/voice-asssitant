import ollama

def get_ai_response(user_input,name ,personality):
     model_name = "qwen2.5:0.5b"
     prompt = f"your name{name} with {personality}, answer according to your personality."

     response = ollama.chat(
          model= model_name,
         messages=[
               {"role":"system", "content":prompt},
               {"role":"user", "content":user_input}
         ]
     )

     return response["message"]["content"] if "message" in response else "tidak ada response"