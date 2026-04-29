#!/bin/bash

#Asks for the criteria of sorting leaderboard using dialog command
criteria=$(dialog --stdout --menu "Choose Sorting option:" 15 40 4 \
1 "Name" \
2 "Game" \
3 "Wins" \
4 "Loss" \
5 "Win-loss ratio" \
)

if [[ "$criteria" == "2" ]]; then
    sortby="sort -t$'\t' -k2,2"
elif [[ "$criteria" == "3" ]]; then
    sortby="sort -t$'\t' -k3,3nr"
elif [[ "$criteria" == "4" ]]; then
    sortby="sort -t$'\t' -k4,4nr"
elif [[ "$criteria" == "5" ]]; then
    sortby="sort -t$'\t' -k5,5nr"
else
    sortby="sort -t$'\t' -k1,1"
fi

awk -F, '
BEGIN{
    printf "\n\n                               Leaderboard\n\n"
    printf "%-15s\t%-15s\t%-10s\t%-10s\t%-20s\n", "Player", "Game", "Wins", "Losses", "Win/Losses Ratio" #Heading of the leaderboard
    printf "---------------------------------------------------------------------------------\n"
}'

awk -F, '
BEGIN{
    FS = "," ; OfS = "\t" 
}
{
    if(NR==1){next}
    win = $1
    los = $2
    game = $3

    wins[win,game]++ #Stores the number of times a particular player has won per game
    loss[los,game]++ #Stores the number of times a particular player has lost per game
    pla[win","game] = 1 #Stores the names of player who has won a particular game
    pla[los","game] = 1 #Stores the names of player has lost a particular game
}
END{
    for (i in pla){
        split(i, arr, ",")
        player = arr[1]
        game = arr[2]
        printf "%-15s\t%-15s\t%-10d\t%-10d\t%-20.2f\n", player, game, wins[player,game], loss[player,game], (loss[player,game]==0? wins[player,game] : wins[player,game]/loss[player,game])
    }
}' history.csv | eval "$sortby"
printf "\n"
