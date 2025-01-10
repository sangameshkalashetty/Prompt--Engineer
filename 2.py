def create_prompt():
        topic=input("what is the topic for the stpry?")
        prompt=input("Enter the tone(serious,humorous,adventurous,funny,sad):")

        prompt=f"write a {tone} story about {topic}."
        return prompt

user_prompt=create_prompt
print("Generated prompt:",user_prompt)