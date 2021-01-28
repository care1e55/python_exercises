def run_timing():
    acummulator = 0
    run_counter = 0
    while True:
        one_run_time = input("Enter 10 km run time: ")
        if not one_run_time:
            break
        try:
            acummulator += float(one_run_time)
        except ValueError:
            print("Invalid input")
            continue
        run_counter += 1
        continue
    result = acummulator/run_counter
    print(f"Average of {result:.2f} over {run_counter} runs")



if __name__=="__main__":
    run_timing()
