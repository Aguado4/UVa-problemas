# Name: Juan José Aguado
#This was my first programming problem so it may not pass UVa online judge tests or similar tests
# November 27, 2020
# Problem: https://onlinejudge.org/external/1/139.pdf Telephone Tangles
# Input: It has 2 parts; the first one is a set of data consisting of
## a code, a space, the locality, a "$", and the price in cents per minute
## (for each line until 000000 is written, then another series of lines
## containing the dialed number and the duration
# Conditions:
# International max=2+3+10=15/min=2+1+4=7, starts with 00
# National max=1+5+7=13/min/1+1+4=6, starts with 0
# Output: For each line, it consists of the dialed number, locality, subscriber number
## (dialed number without the code), duration, price per minute, and the
## total cost of the call (duration*(PPM/100))

def unknown(called, duration):
    l = ["Unknown", called, " ", duration, " ", "-1.00"]  # Unknown locality, dialed number, if the locality is unknown, leave it empty,
    # duration, if the locality is unknown, leave it empty, if the locality is unknown, put -1.00
    return l

def resolve(LCP, called, duration):
    final = []
    for i in range(len(called)):
        l = []
        if called[i][0] != "0" or len(called[i]) < 2:  # i.e., if the call is local (local calls start with any number other than 0)
            l = ["Local", called[i], called[i], duration[i], "0.00", "0.00"]  # number, number without code (since it's local, it's the normal number), duration, cost per
            # minute (as it's local, it's free), total cost (as it's local, it's free)
            final.append(l)  # add elements to the final list
        else:
            if called[i][1] == "0" and len(called[i]) > 15 or called[i][1] == "0" and len(called[i]) < 7:  # if the international number does not match the conditions
                final.append(unknown(called[i], duration[i]))
                k = True
            elif called[i][1] != "0" and len(called[i]) > 13 or called[i][1] != "0" and len(called[i]) < 6:  # if the national number does not match the conditions
                final.append(unknown(called[i], duration[i]))
                k = True
            else:
                k = False
                for j in range(len(LCP)):
                    if LCP[j][1] in called[i][:len(LCP[j][1])]:  # i.e., if the dialed number has a known code within the first numbers
                        if called[i][1] == "0" and (len(called[i]) - len(LCP[j][1])) < 4 or called[i][1] == "0" and (len(called[i]) - len(LCP[j][1])) > 10:
                            final.append(unknown(called[i], duration[i]))
                            k = True  # i.e., if the subscriber number is less/greater than expected
                        elif called[i][1] != "0" and (len(called[i]) - len(LCP[j][1])) < 4 or called[i][1] != "0" and (len(called[i]) - len(LCP[j][1])) > 7:
                            final.append(unknown(called[i], duration[i]))
                            k = True  # i.e., if the subscriber number is less/greater than expected
                        else:
                            k = True
                            x = called[i].split(LCP[j][1])  # split the number from the code/subtract code len
                            l = [LCP[j][0], called[i], x[1], duration[i], str("%.2f" % (LCP[j][2] / 100)),
                                 str("%.2f" % (LCP[j][2] / 100 * duration[i]))]  # locality, dialed number,
                            # dialed number without code, duration, price in dollars as string with two decimals,
                            # total price in dollars as string with two decimals
                            final.append(l)  # add elements to the final list
                            called[i] = "Changed to avoid repetition, I know it's not elegant but I couldn't figure out a better way and remove didn't work"
            if k == False:  # i.e., if the dialed number is not local and does not match any code
                final.append(unknown(called[i], duration[i]))  # add elements to the final list
    for d in range(len(final)):
        print("%-15s %-25s%10s %4s %5s %6s" % (final[d][1], final[d][0], final[d][2], final[d][3], final[d][4], final[d][5]))

def readPrint():
    LCP, called, duration = [], [], []  # create all the lists in which the data will be stored. LCP=LocalityCodePrice
    w = input()
    while w != "000000":  # ask for data until 000000 is entered to proceed to another part
        l = []
        x = w.split("$")  # split the price from the rest to separate it into a list later
        y = x[0].index(" ")  # define the position of the first space
        l = [x[0][y + 1:], x[0][:y], int(x[1])]  # add before the first space, after it excluding the price, and
        # add prices as integers to operate with them later
        LCP.append(l)
        w = input()  # ask for the next data
    w = input()
    while w != "#":  # ask for data until # is entered to indicate the end of the input
        x = w.split()  # separate the dialed number from the duration and add them to their respective lists
        called.append(x[0])
        duration.append(int(x[1]))  # add the duration as an integer to operate with it later
        w = input()
    resolve(LCP, called, duration)

readPrint()
