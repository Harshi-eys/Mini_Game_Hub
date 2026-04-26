awk -F, '
BEGIN{
    FS = "," ; OfS = "\t" 
}
{
    if(NR==1){next}
    name[NR] = $1
    ttt_W[NR] = $2
    ttt_L[NR] = $3
    oth_W[NR] = $4
    oth_L[NR] = $5
    c4_W[NR] = $6
    c4_L[NR] = $7

}
END{
    print "TIC TAC TOE:"
    printf "%-15s %-10s %-10s %-20s\n", "Names", "Wins", "Losses", "Win/Losses Ratio"
    for (i=2; i<=NR; i++){
        printf "%-15s %-10d %-10d %-10.2f\n", name[i], ttt_W[i], ttt_L[i], (ttt_L[i] == 0 ? ttt_W[i] : ttt_W[i] / ttt_L[i])
    }

    print "\n"
    print "OTHELLO:"
    printf "%-15s %-10s %-10s %-20s\n", "Names", "Wins", "Losses", "Win/Losses Ratio"
    for (i=2; i<=NR; i++){
        printf "%-15s %-10d %-10d %-10.2f\n", name[i], oth_W[i], oth_L[i], (oth_L[i] == 0 ? oth_W[i] : oth_W[i] / oth_L[i])
    }

    print "\n"
    print "CONNECT4:"
    printf "%-15s %-10s %-10s %-20s\n", "Names", "Wins", "Losses", "Win/Losses Ratio"
    for (i=2; i<=NR; i++){
        printf "%-15s %-10d %-10d %-10.2f\n", name[i], c4_W[i], c4_L[i], (c4_L[i] == 0 ? c4_W[i] : c4_W[i] / c4_L[i])
    }

}
' history.csv