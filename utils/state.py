reply_states = {}

def set_reply(admin_id, user_id):
    reply_states[str(admin_id)] = user_id

def get_reply(admin_id):
    return reply_states.get(str(admin_id))

def clear_reply(admin_id):
    reply_states.pop(str(admin_id), None)
