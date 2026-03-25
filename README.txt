Mini_Game_Hub

This project is a multi-user game hub built using Bash and Python (Pygame).

The following are the different components of this project:-

Main Components:
- main.sh: Authenticates two users using SHA-256 hashing and saves them to users.tsv
- game.py: Runs the game menu, handles gameplay and manages results.
- leaderboard.sh: Shows results of the players from history.csv.

Games Included:
- Tic Tac Toe 
- Othello(reversi)
- Connect Four

How does it function??
1. Run `bash main.sh`
2. Users log in
3. Game menu is displayed
4. Players select and play a game
5. Results are stored and leaderboard is shown

Files:
- users.tsv: Stores user credentials
- history.csv: Stores game results
