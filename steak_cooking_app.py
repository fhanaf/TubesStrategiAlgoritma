import streamlit as st

def solveWithGreedy(N, T, A, B):
    totalTime = 0

    for i in range(N - 1, 0, -1):
        neededSteaks = B[i] - A[i]
        if neededSteaks > 0:
            additionalTime = neededSteaks * T[i - 1]
            totalTime += additionalTime
            A[i] += neededSteaks
            A[i - 1] -= neededSteaks

    for i in range(N):
        if A[i] < B[i]:
            return -1

    return totalTime

def dynamic_programming(N, T, A, B):
    memo = {}

    def dp(steak_counts):
        if tuple(steak_counts) in memo:
            return memo[tuple(steak_counts)]
        if all(steak_counts[i] >= B[i] for i in range(N)):
            return 0

        min_time = float('inf')
        for i in range(N - 1):
            if steak_counts[i] > 0:
                new_steak_counts = steak_counts[:]
                new_steak_counts[i] -= 1
                new_steak_counts[i + 1] += 1
                time = T[i] + dp(new_steak_counts)
                min_time = min(min_time, time)

        memo[tuple(steak_counts)] = min_time
        return min_time

    total_time = dp(A)

    if total_time == float('inf'):
        return -1
    else:
        return total_time

    
def main():
    st.title("Steak House Orders Fulfillment")

    st.sidebar.header("Input Parameters")

    N = st.sidebar.number_input("Number of Doneness Levels:", min_value=2, max_value=100000, step=1)
    
    st.sidebar.header("Cooking Time")
    T = []
    for i in range(N - 1):
        T.append(st.sidebar.number_input(f"Level {i+1} to Level {i+2}:", min_value=1, max_value=1000, step=1))

    st.sidebar.header("Initial Steak Counts at Steak House")
    A = []
    for i in range(N):
        A.append(st.sidebar.number_input(f"Doneness Level A{i+1}:", min_value=0, max_value=1000, step=1))

    st.sidebar.header("Orders at Steak House")
    B = []
    for i in range(N):
        B.append(st.sidebar.number_input(f"Doneness Level B{i+1}:", min_value=0, max_value=1000, step=1))

    choice = st.multiselect('Choose Algorithm',['Greedy', 'Dynamic Programming'], default=['Greedy', 'Dynamic Programming'])
    
    if st.button("Calculate Total Time"):
        if 'Greedy' in choice:
            total_time_greedy = solveWithGreedy(N, T, A, B)
            if total_time_greedy == -1:
                st.error("It is not possible to cook the steaks at both restaurants using Greedy method.")
            else:
                st.success("The total time needed to cook all steaks at both restaurants using Greedy method is possible")
        if 'Backtracking' in choice:
            total_time_DP = dynamic_programming(N, T, A, B)
            if total_time_DP == -1:
                st.error("It is not possible to cook the steaks at both restaurants using Dynamic Programming method.")
            else:
                st.success("The total time needed to cook all steaks at both restaurants using Dynamic Programming method is possible")
        if total_time_greedy != -1:
            st.header("With Total Time : ")
            st.header(total_time_greedy)

if __name__ == "__main__":
    main()
