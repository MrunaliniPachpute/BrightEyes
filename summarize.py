from openai import AzureOpenAI
import os

# Initialize client with proper config
client = AzureOpenAI(
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_APIKEY")
)

DEPLOYMENT_NAME =os.getenv("DEPLOYMENT_NAME")

def summarize_text(text):
    prompt = f"Summarize this text for a visually impaired user in simple language:\n{text}"

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )

    summary = response.choices[0].message.content.strip()
    return summary
