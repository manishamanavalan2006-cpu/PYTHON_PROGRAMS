def orangecap(d):
    totals = {}   
    for match in d:
        for player in d[match]:
            if player in totals:
                totals[player] += d[match][player]
            else:
                totals[player] = d[match][player]
    top_player = ""
    top_score = 0


    for player in totals:
        if totals[player] > top_score:
            top_score = totals[player]
            top_player = player
    
    return (top_player, top_score)

{#input basis
 'match1':{'player1':57, 'player2':38},
 'match2':{'player3':9, 'player1':42},
 'match3':{'player2':41, 'player4':63, 'player3':91}
}