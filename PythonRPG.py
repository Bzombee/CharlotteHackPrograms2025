import random

def fight():
    """Handles a simple battle between the player and a goblin."""
    player_health = 100
    goblin_health = 50
    
    print("\nA wild goblin appears!")
    
    while player_health > 0 and goblin_health > 0:
        print(f"\nYour HP: {player_health} | Goblin HP: {goblin_health}")
        
        action = input("Do you want to (1) Attack or (2) Run? ")
        
        if action == "1":
            #player attack
            player_damage = random.randint(10,20)
            print(f"You hit the goblin for {player_damage} damage!")
            goblin_health -= player_damage
            
            # If goblin is still alive, it attacks back
            if goblin_health > 0:
                goblin_damage = random.randint(5,15)
                print(f"The goblin strikes back for {goblin_damage} damage!")
                player_health -= goblin_damage
            
        elif action == "2":
            print("You successfully escape!")
            return
        else:
            print("Invalid action, please enter 1 to Attack or 2 to Run.")
    
    #Results of fighting
    if player_health <= 0:
        print("\nYou have been defeated... Game Over!")
    else:
        print("\nYou defeated the goblin!")

#Main code
def start_game():
    print("\nWelcome, traveler! You enter a dark forest.")
    
    choice = input("Do you want to (1) Explore the ruins or (2) Cross the river? ")
    
    if choice == "1":
        fight()
    elif choice == "2":
        print("Test")
    else:
        print("Invalid choice. Your adventure ends here.")
    
    
while True:
    start_game()
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
    
    #"    attack    ".strip() = "attack"
    #"ATTACK".lower() = "attack"
    #"   ATTACK   ".strip.lower() = "attack"
    # 1 != 2 is True
    # 1 != 1 is False