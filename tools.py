from datetime import datetime


def get_current_tim():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_tim",
            "description": "Get the current time in the format DD-MM-YYYY HH:MM:SS",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]