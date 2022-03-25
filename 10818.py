n = int(input())
n_list = list(map(int,input().split()))

#N_list의 값을 오름차순으로 정렬한다.
n_list.sort()

#정렬된 수 중 가장 첫번째 수가 최소, 가장 나중 수가 최대가 된다
#배열 값은 0부터 시작한다. 따라서 만약 N이 5라면 인덱스 값은 6이 되므로 N-1을 해줘야 정확한 인덱스값을 구할 수 있다.
print(n_list[0], n_list[n-1])
