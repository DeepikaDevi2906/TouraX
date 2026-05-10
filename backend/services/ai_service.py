from langchain_agent.agent import agent

chat_history = []
def generate_ai_response(
    user_message
):

    global chat_history

    try:

        response = agent.invoke({

            "input": user_message,

            "chat_history": chat_history
        })

        chat_history.append(
            (user_message, response["output"])
        )

        return {

            "type": "chat",

            "message":
                response["output"]
        }

    except Exception as e:

        return {

            "type": "chat",

            "message":
                f"AI Error: {str(e)}"
        }