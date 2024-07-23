from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])

    direction_y = [-1, 1, 0, 0]
    direction_x = [0, 0, -1, 1]

    def bfs(start, goal):
        visited = [[0] * cols for _ in range(rows)]  # 방문 체크
        queue = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = 1

        while queue:
            current_y, current_x, steps = queue.popleft()

            if (current_y, current_x) == goal:  # 목표지점에 도달한 경우
                return steps

            for direction in range(4):
                next_y = current_y + direction_y[direction]
                next_x = current_x + direction_x[direction]

                if 0 <= next_y < rows and 0 <= next_x < cols and maps[next_y][next_x] != 'X' and visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = 1
                    queue.append((next_y, next_x, steps + 1))

        return 0

    positions = [(), (), ()]  # 좌표 저장 [시작 지점, 레버, 출구]

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                positions[0] = (i, j)
            elif maps[i][j] == 'L':
                positions[1] = (i, j)
            elif maps[i][j] == 'E':
                positions[2] = (i, j)

    distance_to_lever = bfs(positions[0], positions[1])  # 출발 지점 -> 레버
    distance_to_exit = bfs(positions[1], positions[2])   # 레버 -> 출구

    if distance_to_lever and distance_to_exit:  # 둘 다 도착하는 경우에만 최종적으로 탈출이 가능
        return distance_to_lever + distance_to_exit
    else:
        return -1