def sqInRect(lng, wdth):
    lng_temp = lng
    wdth_temp = wdth
    squares = []

    if lng is wdth:
        return None
    else:
        while lng_temp and wdth_temp is not 0:
            if lng_temp > wdth_temp:
                squares.append(wdth_temp)
                lng_temp -= wdth_temp
            elif lng_temp < wdth_temp:
                squares.append(lng_temp)
                wdth_temp -= lng_temp
            elif wdth_temp is lng_temp:
                squares.append(wdth_temp)
                lng_temp = 0
                wdth_temp = 0
            else:
                print('Error!')
                break
            print(squares)                              # for debug
            print(lng_temp, wdth_temp)      # for debug
        return squares

sqInRect(5, 3)
