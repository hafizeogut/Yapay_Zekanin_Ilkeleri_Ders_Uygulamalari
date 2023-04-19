import gym

# Fayda tabanlı ajanımız
class FaydaTabanliAjan:
    def __init__(self, action_space):
        self.action_space = action_space
        self.q_table = {}

    # Q-tablosuna göre eylem seçimi
    def act(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        return self.action_space.sample() if self.q_table[state][0] == self.q_table[state][1] else self.q_table[state].index(max(self.q_table[state]))

    # Q-tablosu güncelleme
    def update_q_table(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        self.q_table[state][action] += 0.1 * (reward + 0.99 * max(self.q_table[next_state]) - self.q_table[state][action])

# CartPole oyun ortamı
env = gym.make('CartPole-v0')

# Ajan ve değişken tanımları
fayda_tabanli_ajan = FaydaTabanliAjan(env.action_space)
num_episodes = 1000

# Eğitim döngüsü
for i in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action = fayda_tabanli_ajan.act(str(state))
        next_state, reward, done, _ = env.step(action)
        total_reward += reward
        fayda_tabanli_ajan.update_q_table(str(state), action, reward, str(next_state))
        state = next_state
    print(f"Episode {i+1} - Total Reward: {total_reward}")

env.close()
