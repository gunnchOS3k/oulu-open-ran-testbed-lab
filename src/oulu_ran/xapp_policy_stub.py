def policy(state):
    return {'slice': 'eMBB' if state.get('load',0)<0.7 else 'URLLC'}
