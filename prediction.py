import vari


def predict(match1, dictList, dictChart):

        matchKey1 = getattr(match1, "key")
        alliances1 = getattr(match1, "alliances")
        redScore1 = alliances1[vari.red]["score"]
        blueScore1 = alliances1[vari.blue]["score"]
        # matchNumber = int(getattr(match1, "match_number"))
        # If the match hasn't been played yet
        if redScore1 == -1 or blueScore1 == -1:
            print("Predicting Match" + matchKey1)
            blueTeam1 = alliances1[vari.blue][vari.teamKeys][0]
            blueTeam2 = alliances1[vari.blue][vari.teamKeys][1]
            blueTeam3 = alliances1[vari.blue][vari.teamKeys][2]
            redTeam1 = alliances1[vari.red][vari.teamKeys][0]
            redTeam2 = alliances1[vari.red][vari.teamKeys][1]
            redTeam3 = alliances1[vari.red][vari.teamKeys][2]
            # trim teams down to just numbers
            bT1Number = blueTeam1[3:]
            bT2Number = blueTeam2[3:]
            bT3Number = blueTeam3[3:]
            rT1Number = redTeam1[3:]
            rT2Number = redTeam2[3:]
            rT3Number = redTeam3[3:]

            # Predict the scores
            """dictList ={teamNumber: [teamNumber [0], teamName[1], matchCount[2], totalRP[3], winPercent[4], vgMobility[5],
                        avgAutoSwitch[6], avgAutoScale[7], avgTeleSwitch[8], avgTeleOppSwitch[9], avgTeleScale[10], 
                        avgVault[11], avgClimb[12], avgLevitate[13], avgPark[14], avgFoulPoints[15], avgPoints[16], 
                        bestLink[17], worstLink[18]]}

               dictChart =avgVault * 5[6], frc(avgClimb * 30)[7], frc(avgLevitate * 30)[8], frc(avgPark * 5)[9]"""
            # Blue Predicted Points
            blueMobility = (dictList[int(bT1Number)][5] + dictList[int(bT2Number)][5] + dictList[int(bT3Number)][5]) / 3
            blueAutoSwitch = (dictList[int(bT1Number)][6] + dictList[int(bT2Number)][6] +
                              dictList[int(bT3Number)][6]) / 3
            blueAutoScale = (dictList[int(bT1Number)][7] + dictList[int(bT2Number)][7] + dictList[int(bT3Number)][
                7]) / 3
            blueTeleSwitch = (dictList[int(bT1Number)][8] + dictList[int(bT2Number)][8] + dictList[int(bT3Number)][
                8]) / 3
            blueOppSwitch = (dictList[int(bT1Number)][9] + dictList[int(bT2Number)][9] + dictList[int(bT3Number)][
                9]) / 3
            blueTeleScale = (dictList[int(bT1Number)][10] + dictList[int(bT2Number)][10] + dictList[int(bT3Number)][
                10]) / 3
            blueVault = (dictList[int(bT1Number)][11] + dictList[int(bT2Number)][11] + dictList[int(bT3Number)][
                11]) * 5 / 3
            blueEndGame = (dictChart[int(bT1Number)][7] + dictChart[int(bT2Number)][7] + dictChart[int(bT3Number)][7] +
                           dictChart[int(bT1Number)][8] + dictChart[int(bT2Number)][8] + dictChart[int(bT3Number)][8] +
                           dictChart[int(bT1Number)][9] + dictChart[int(bT2Number)][9] + dictChart[int(bT3Number)][
                               9]) / 3
            blueFouls = (dictList[int(bT1Number)][15] + dictList[int(bT2Number)][15] + dictList[int(bT3Number)][15]) / 3

            # Red predicted points
            redMobility = (dictList[int(rT1Number)][5] + dictList[int(rT2Number)][5] + dictList[int(rT3Number)][5]) / 3
            redAutoSwitch = (dictList[int(rT1Number)][6] + dictList[int(rT2Number)][6] +
                             dictList[int(rT3Number)][6]) / 3
            redAutoScale = (dictList[int(rT1Number)][7] + dictList[int(rT2Number)][7] + dictList[int(rT3Number)][7]) / 3
            redTeleSwitch = (dictList[int(rT1Number)][8] + dictList[int(rT2Number)][8] + dictList[int(rT3Number)][
                8]) / 3
            redOppSwitch = (dictList[int(rT1Number)][9] + dictList[int(rT2Number)][9] + dictList[int(rT3Number)][9]) / 3
            redTeleScale = (dictList[int(rT1Number)][10] + dictList[int(rT2Number)][10] + dictList[int(rT3Number)][
                10]) / 3
            redVault = (dictList[int(rT1Number)][11] + dictList[int(rT2Number)][11] + dictList[int(rT3Number)][
                11]) * 5 / 3
            redEndGame = (dictChart[int(rT1Number)][7] + dictChart[int(rT2Number)][7] + dictChart[int(rT3Number)][7] +
                          dictChart[int(rT1Number)][8] + dictChart[int(rT2Number)][8] + dictChart[int(rT3Number)][8] +
                          dictChart[int(rT1Number)][9] + dictChart[int(rT2Number)][9] + dictChart[int(rT3Number)][
                              9]) / 3
            redFouls = (dictList[int(rT1Number)][15] + dictList[int(rT2Number)][15] + dictList[int(rT3Number)][15]) / 3

            bluePredictedScore = (
                        blueMobility + blueAutoSwitch + blueAutoScale + (blueTeleSwitch + abs(redOppSwitch)) / 2 +
                        blueTeleScale + blueVault + blueEndGame + abs(redFouls))
            redPredictedScore = (redMobility + redAutoSwitch + redAutoScale + (redTeleSwitch + abs(blueOppSwitch)) / 2 +
                                 redTeleScale + redVault + redEndGame + abs(blueFouls))

            if bluePredictedScore > redPredictedScore:
                predictWinner = vari.blue
            elif bluePredictedScore < redPredictedScore:
                predictWinner = vari.red
            else:
                predictWinner = "tie"

            # Build Dictionary
            predictList = [matchKey1, predictWinner, bT1Number, bT2Number, bT3Number, bluePredictedScore,
                           redPredictedScore,
                           rT1Number, rT2Number, rT3Number]

            return predictList
