def menu(**kwargs):
    greet = f'Possible inputs are: {"/".join(kwargs.keys())}\n'
    try:
        return kwargs[input(greet)]()
    except:
        print("Not in list of valid inputs")
