import random

def play():
    user = input("pilih antara (kertas, batu, dan gunting): ").lower()
    computer = random.choice(['batu', 'kertas', 'gunting'])
    
    print(f"computer memilih: {computer}")
    
    if user == computer:
        return "ini seri!"
    if is_win(user, computer):
        return "kamu menang"
    return "kamu kalah"
    
def is_win(player, opponent):
    return (
               (player == 'batu' and opponent == 'gunting') or
               (player == 'gunting' and opponent == 'kertas') or
               (player == 'kertas' and opponent == 'batu')
    )
    
print(play())
     
