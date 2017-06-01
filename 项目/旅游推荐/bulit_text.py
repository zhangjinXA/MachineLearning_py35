def bulitText(data):
    text = '<p></p>'
    for i in range(len(data.index)):
        line1 = ''
        for ii in range(len(data.columns)):
            line1 = line1 + '  **  ' + str(data.iloc[i, ii])
        text = text + '<p>' + line1 + '</p>'
    return text

def builtLine(LineData):
    LineData = LineData.values
    line = ''
    for ii in range(len(LineData)):
        line = line + ' ** ' + str(LineData[ii])
    return line