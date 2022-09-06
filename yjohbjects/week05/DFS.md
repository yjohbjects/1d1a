# DFS

### **DFS** (깊이 우선 탐색) - 후입선출

- 말그대로 깊은 부분을 우선적으로 탐색하는 알고리즘
- 자기 자신을 호출하는 순환 알고리즘의 형태 를 가지고 있다.
- 주로 백트래킹에 사용
- 속도
    - 단순 검색: DFS < BFS
    - 순회: DFS > BFS

![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled.png)

### **DFS 활용 방안**

- 1차원 리스트
  
    ![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled%201.png)
    
    ```python
    def DFS(x):
        visited[x] = 1
        for j in links[x]:
            if visited[j] != 1: # 방문하지 않았다면
                DFS(j)
    ```
    
- 2차원 리스트
  
    ![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled%202.png)
    
    ```python
    def DFS(x, y):
        dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 델타이동 (상, 하, 좌, 우)
    
        for q in range(4):
            dx = x + dxy[q][0]
            dy = y + dxy[q][1]
    
            # 맵 밖의 위치를 탐색하면 pass
            if dx < 0 or dx >= height or dy < 0 or dy >= width:
                continue
            # 방문한 적 없고, 배추가 있으면 DFS 함수 안으로
            elif visited[dx][dy] == 0 and field[dx][dy] == 1:
                visited[dx][dy] = 1 # 방문도장
                DFS(dx, dy) # 탐색
    ```
    

### 동작 과정

**후입선출**

1. 탐색 노드를 스택에 삽입하고 방문 처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 그 인접 노드를 스택에 넣고 방문 처리를 합니다. 방문하지 않은 인접 노드가 없으면 최상단 노드를 꺼냅니다.
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복합니다.
- While (iterative)
  
    ```python
    stack = [1] # 1은 시작점  
    while stack: 
        pin = stack[-1]
        visited[pin] = 1
        for com in links[pin]:
            if visited[com] != 0: # 방문하지 않았다면
                stack.append(com) # stack에 저장
                break
        else:
            stack.pop() 
    ```
    
- 함수
  
    ```python
    def DFS(x):
        visited[x] = 1
        for j in links[x]:
            if visited[j] != 1: # 방문하지 않았다면
                DFS(j) # 다음 루트로
    ```
    
          *⇒ B2606 바이러스 문제로 설명 예시*
    

### **특징**

**장점**

- 경로상의 노드, 즉 스택으로 필요한 경로만 저장하기 때문에 저장공간을 덜 차지한다
- A → B까지 출발점과 도착점이 주어진다면 최적의 알고리즘이 아닐까?

**단점**

- 무한 루프에 빠질 수가 있다… (방문도장 잘 확인하기)
- 최단경로라는 보장은 없다
- BFS보다 수요가 적다?

⇒ 최단경로 X, A→B까지 출발점과 도착점이 지정되어있는 문제에 최적

⇒ A→B 활용 가능 문제: 사이의 경로 저장, 사이 경로의 수

- (번외) **순서의 다양성** (이부분은 Tree에서 더 배우게 될 것입니다람쥐 . . .)
    - **전위 순회**: preorder (Root → L → R)
    
    ![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled.png)
    
    - **중위 순회:** inorder (L → Root → R)
    
    ![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled.png)
    
    - **후위 순회**: postorder (L → R → Root)
    
    ![Untitled](week05%207dcc06561d294160bec68af8a0409b68/Untitled.png)
    
    [과정을 자세히 보고싶다면 …?](https://livecoding.tistory.com/46)
    
    1. 레벨 순서 순회 (level-order)
        - 모든 노드를 낮은 레벨부터 차례대로 순회. (=BFS)
    

---

*출처*

[https://butter-shower.tistory.com/223](https://butter-shower.tistory.com/223)

[https://miiinnn23.tistory.com/14](https://miiinnn23.tistory.com/14)

---

