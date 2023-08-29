import chainlit as cl
#conda install -c conda-forge textblob
from textblob import TextBlob
# export OPENAI_API_KEY="..."
from langchain.chat_models import ChatOpenAI
chat_model=ChatOpenAI()

# continuously on a loop
@cl.on_message
async def main(message:str):
          if "sentiment" in message:
            files=None

            while files==None:
                files=await cl.AskFileMessage(content="Please upload a text file to analyse",accept=["text/plain"]).send()
            file=files[0]
            msg = cl.Message(content=f"Processing `{file.name}`...")
            await msg.send()
            text=file.content.decode("utf-8")
            blob=TextBlob(text)

            await cl.Message(
                        content=f"Sure,here is your analysis: {text},\n your result is {blob.sentiment}",
                    ).send()
          else:
            result=chat_model.predict(message)
            message=result

            await cl.Message(
                content=f"{message}",
            ).send()


@cl.on_chat_start
async def start():
    content="Hello I am SentimentAI"
    await cl.Message(content=content,).send()

