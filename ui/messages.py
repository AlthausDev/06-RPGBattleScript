from ui.colors import Bcolors

def combat_start_message(enemy_name):
    print(f"{Bcolors.FAIL}{Bcolors.BOLD}An Enemy ({enemy_name}) is attacking you!{Bcolors.ENDC}")

def display_victory_message(enemy_name):
    print(f"{Bcolors.OKGREEN}{Bcolors.BOLD}YOU WIN! {enemy_name} has been defeated!{Bcolors.ENDC}")

def display_defeat_message(player_name):
    print(f"{Bcolors.FAIL}{Bcolors.BOLD}{player_name} has been defeated. YOU LOSE!{Bcolors.ENDC}")
