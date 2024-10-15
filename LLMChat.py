import autogen
import json
from autogen import AssistantAgent, Agent, UserProxyAgent, ConversableAgent

class ChatAssistant:
    def __init__(self, config_file_path: str = "./OAI_CONFIG_LIST.json"):
        # Load configuration lists based on models
        self.config_list_gemini = autogen.config_list_from_json(
            config_file_path,
            filter_dict={
                "model": ["gemini-pro"],
            },
        )

        # Initialize assistant and user proxy agents
        self.assistant = AssistantAgent("assistant",
                                        llm_config={"config_list": self.config_list_gemini, "seed": 42},
                                        max_consecutive_auto_reply=1)

        self.user_proxy = UserProxyAgent("user_proxy",
                                         code_execution_config={"work_dir": "coding", "use_docker": False},
                                         human_input_mode="NEVER",
                                         is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0)

        self.dummy_code_writer = AssistantAgent("assistant",
                                                llm_config={"config_list": self.config_list_gemini, "seed": 42},
                                                max_consecutive_auto_reply=1)

    def initiate_chat(self, message: str) -> str:
        # Initiate chat between user proxy and assistant
        result = self.dummy_code_writer.initiate_chat(self.assistant, message=message)
        print("***********************************")
        print(result)
        print("***********************************")
        resp = result.summary
        print(result.chat_history[-1])
        if len(resp) == 0:
            resp = result.chat_history[-1]['content']
            if resp == 'TERMINATE' and len(result.chat_history) > 1:
                resp = result.chat_history[-2]['content']
            resp = resp.replace('TERMINATE', '')
            if len(resp) == 0 or resp == 'TERMINATE':
                resp = "No response from server. Try another query"

        # Return response as a string
        return resp

# chat = ChatAssistant("/path/to/OAI_CONFIG_LIST.json")
# response = chat.initiate_chat("Sort the array with Merge Sort: [4, 1, 3, 2]")
# print(response)
