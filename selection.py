def selection(options, selection):
    num_options = len(options)
    counter = 1
    while counter <= num_options:
        print("{}. {}".format(counter, options[counter-1]))
        counter += 1
    selection = input()
    try:
        selection = int(selection)
        if selection <= num_options and selection > 0:
            return options, options[selection-1]
        else:
            print("Invalid input %r" % selection)
    except:
        print("Invalid input %r" % selection)