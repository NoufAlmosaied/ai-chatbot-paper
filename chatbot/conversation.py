class ConversationManager:
    def __init__(self):
        self.sessions = {}
    
    def process_message(self, session_id, message):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(message)
        return {"response": "Message received"}
