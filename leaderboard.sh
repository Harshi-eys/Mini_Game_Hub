awk -F, '
BEGIN{
    printf "\n                             Leaderboard\n"
    printf "%-20s %-15s %-10s %-10s %-20s\n", "Player", "Game", "Wins", "Losses", "Win/Losses Ratio"
    printf "----------------------------------------------------------------------------\n"
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

    wins[win,game]++
    loss[los,game]++
    pla[win","game] = 1
    pla[los","game] = 1
}
END{
    for (i in pla){
        split(i, arr, ",")
        player = arr[1]
        game = arr[2]
        printf "%-20s %-15s %-10d %-10d %-20.2f\n", player, game, wins[player,game], loss[player,game], (loss[player,game]==0? wins[player,game] : wins[player,game]/loss[player,game])
    }
}' history.csv | sort 
printf "\n"
