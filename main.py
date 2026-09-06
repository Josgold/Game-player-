import random
import time

def select_action(best_action, alternative_actions):
    # 90% chance to choose the optimal move, 10% chance to make a "mistake"
    if random.random() < 0.90:
        return best_action
    else:
        # Pick a secondary, sub-optimal action
        return random.choice(alternative_actions)

def human_reaction_delay():
    # Mean reaction time of ~250ms with a standard deviation of 50ms
    delay = random.gauss(0.25, 0.05)
    # Ensure delay stays within realistic human limits
    delay = max(0.15, min(delay, 0.60))
    time.sleep(delay)
