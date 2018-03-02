import vari


def predict(match1, dictlist, dictchart):

        matchkey = getattr(match1, "match_number")
        alliance = getattr(match1, "alliances")
        redscore = alliance[vari.red]["score"]
        bluescore = alliance[vari.blue]["score"]
        # matchNumber = int(getattr(match1, "match_number"))
        # If the match hasn't been played yet
        if not vari.isplayed(redscore, bluescore):
            print("Predicting Match" + str(matchkey))
            # trim teams down to just numbers
            bt1number = vari.teamid(alliance, vari.blue, 1)
            bt2number = vari.teamid(alliance, vari.blue, 2)
            bt3number = vari.teamid(alliance, vari.blue, 3)
            rt1number = vari.teamid(alliance, vari.red, 1)
            rt2number = vari.teamid(alliance, vari.red, 2)
            rt3number = vari.teamid(alliance, vari.red, 3)

            # Predict the scores
            """dictlist ={teamNumber: [teamNumber [0], teamName[1], matchCount[2], totalRP[3], winPercent[4], 
                        vgMobility[5], avgAutoSwitch[6], avgAutoScale[7], avgTeleSwitch[8], avgTeleOppSwitch[9], 
                        avgTeleScale[10], avgVault[11], avgClimb[12], avgLevitate[13], avgPark[14], avgFoulPoints[15], 
                        avgPoints[16], bestLink[17], worstLink[18]]}

               dictchart =avgVault * 5[6], frc(avgClimb * 30)[7], frc(avgLevitate * 30)[8], frc(avgPark * 5)[9]"""
            # Blue Predicted Points
            bluemobility = (dictlist[int(bt1number)][5] + dictlist[int(bt2number)][5] + dictlist[int(bt3number)][5]) / 3
            blueautoswitch = (dictlist[int(bt1number)][6] + dictlist[int(bt2number)][6] +
                              dictlist[int(bt3number)][6]) / 3
            blueautoscale = (dictlist[int(bt1number)][7] + dictlist[int(bt2number)][7] + dictlist[int(bt3number)][
                7]) / 3
            blueteleswitch = (dictlist[int(bt1number)][8] + dictlist[int(bt2number)][8] + dictlist[int(bt3number)][
                8]) / 3
            blueoppswitch = (dictlist[int(bt1number)][9] + dictlist[int(bt2number)][9] + dictlist[int(bt3number)][
                9]) / 3
            bluetelescale = (dictlist[int(bt1number)][10] + dictlist[int(bt2number)][10] + dictlist[int(bt3number)][
                10]) / 3
            bluevault = (dictlist[int(bt1number)][11] + dictlist[int(bt2number)][11] + dictlist[int(bt3number)][
                11]) * 5 / 3
            blueendgame = (dictchart[int(bt1number)][7] + dictchart[int(bt2number)][7] + dictchart[int(bt3number)][7] +
                           dictchart[int(bt1number)][8] + dictchart[int(bt2number)][8] + dictchart[int(bt3number)][8] +
                           dictchart[int(bt1number)][9] + dictchart[int(bt2number)][9] + dictchart[int(bt3number)][
                               9]) / 3
            bluefouls = (dictlist[int(bt1number)][15] + dictlist[int(bt2number)][15] + dictlist[int(bt3number)][15]) / 3

            # Red predicted points
            redmobility = (dictlist[int(rt1number)][5] + dictlist[int(rt2number)][5] + dictlist[int(rt3number)][5]) / 3
            redautoswitch = (dictlist[int(rt1number)][6] + dictlist[int(rt2number)][6] +
                             dictlist[int(rt3number)][6]) / 3
            redautoscale = (dictlist[int(rt1number)][7] + dictlist[int(rt2number)][7] + dictlist[int(rt3number)][7]) / 3
            redteleswitch = (dictlist[int(rt1number)][8] + dictlist[int(rt2number)][8] + dictlist[int(rt3number)][
                8]) / 3
            redoppswitch = (dictlist[int(rt1number)][9] + dictlist[int(rt2number)][9] + dictlist[int(rt3number)][9]) / 3
            redtelescale = (dictlist[int(rt1number)][10] + dictlist[int(rt2number)][10] + dictlist[int(rt3number)][
                10]) / 3
            redvault = (dictlist[int(rt1number)][11] + dictlist[int(rt2number)][11] + dictlist[int(rt3number)][
                11]) * 5 / 3
            redendgame = (dictchart[int(rt1number)][7] + dictchart[int(rt2number)][7] + dictchart[int(rt3number)][7] +
                          dictchart[int(rt1number)][8] + dictchart[int(rt2number)][8] + dictchart[int(rt3number)][8] +
                          dictchart[int(rt1number)][9] + dictchart[int(rt2number)][9] + dictchart[int(rt3number)][
                              9]) / 3
            redfouls = (dictlist[int(rt1number)][15] + dictlist[int(rt2number)][15] + dictlist[int(rt3number)][15]) / 3

            bluepredictedscore = (
                        bluemobility + blueautoswitch + blueautoscale + (blueteleswitch + abs(redoppswitch)) / 2 +
                        bluetelescale + bluevault + blueendgame + abs(redfouls))
            redpredictedscore = (redmobility + redautoswitch + redautoscale + (redteleswitch + abs(blueoppswitch)) / 2 +
                                 redtelescale + redvault + redendgame + abs(bluefouls))

            if bluepredictedscore > redpredictedscore:
                predictwinner = vari.blue
            elif bluepredictedscore < redpredictedscore:
                predictwinner = vari.red
            else:
                predictwinner = "tie"

            # Build Dictionary
            predictlist = [int(matchkey), predictwinner, bt1number, bt2number, bt3number, bluepredictedscore,
                           redpredictedscore,
                           rt1number, rt2number, rt3number]

            return predictlist
