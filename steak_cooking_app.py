import streamlit as st

def solveWithGreedy(N, T, A, B):
    totalTime = 0
    for i in range(N - 1, 0, -1):
        neededSteaks = B[i] - A[i]
        if neededSteaks > 0:
            additionalTime = neededSteaks * T[i - 1]
            totalTime += additionalTime
            print(totalTime)
            A[i] += neededSteaks
            A[i - 1] -= neededSteaks

    for i in range(N):
        if A[i] < B[i]:
            return -1

    return totalTime

def solveWithDynamicProgramming(N, T, A, B):
    dp = [0] * N
    print(N, A[0], A[1], A[2], B[0], B[1], B[2], T[0], T[1])
    for i in range(N - 1, 0, -1):
        neededSteaks = B[i] - A[i]
        if neededSteaks > 0:
            additionalTime = neededSteaks * T[i - 1]
            dp[i - 1] = max(dp[i - 1], dp[i] + additionalTime)
            A[i] += neededSteaks
            A[i - 1] -= neededSteaks
    for i in range(N):
        if A[i] < B[i]:
            return -1
    return dp[0]

def main():
    st.title("Steak House Orders Fulfillment")

    st.sidebar.header("Input Parameters")

    N = st.sidebar.number_input("Number of Doneness Levels:", min_value=2, max_value=100000, step=1)
    M = N
    st.sidebar.header("Cooking Time")
    T = []
    for i in range(N - 1):
        T.append(st.sidebar.number_input(f"Level {i+1} to Level {i+2}:", min_value=1, max_value=1000, step=1))
    X = T
    st.sidebar.header("Initial Steak Counts at Steak House")
    A = []
    for i in range(N):
        A.append(st.sidebar.number_input(f"Doneness Level A{i+1}:", min_value=0, max_value=1000, step=1))
    C = A
    st.sidebar.header("Orders at Steak House")
    B = []
    for i in range(N):
        B.append(st.sidebar.number_input(f"Doneness Level B{i+1}:", min_value=0, max_value=1000, step=1))
    D = B
    choice = st.selectbox(
    "Which Algorithm are you gonna apply?",
    ("Greedy", "Dynamic Programming"))
    if st.button("Calculate Total Time"):
        if 'Greedy' in choice:
            total_time_greedy = solveWithGreedy(N, T, A, B)
            if total_time_greedy == -1:
                st.error("It is not possible to cook the steaks at both restaurants using Greedy method.")
            else:
                st.success("The total time needed to cook all steaks at both restaurants using Greedy method is possible.")
                st.header("the time it cost in Greedy is")
                st.header(total_time_greedy)

        if 'Dynamic Programming' in choice:
            total_time_DP = solveWithDynamicProgramming(N,T,A,B)
            if total_time_DP == -1:
                st.error("It is not possible to cook the steaks at both restaurants using Dynamic Programming method.")
            else:
                st.success("The total time needed to cook all steaks at both restaurants using Dynamic Programming method is possible.")
                st.header("the time it cost in Dynamic Programming is")
                st.header(total_time_DP)


if __name__ == "__main__":
    main()

 
