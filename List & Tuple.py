# List와 Tuple - Python 자료구조
# List와 Tuple은 파이썬에서 데이터를 저장하고 관리하는데 사용되는 가장 기본적인 자료입니다

# 1. index (인덱스)
# 각 항목에 부여된 고유한 번호 (두 가지 세는 방법: positive는 0부터, negative는 -1부터)

# 2. List (리스트)
# 여러 개의 항목을 순서대로 저장할 수 있는 변경 가능한(mutable) 데이터 타입
game = ['overwatch', 'roblox', 'battlegrounds']

# 2-1. 항목 추가하기 (append) - 맨 뒤에 추가
game.append("valorant")

# 2-2. 항목 삽입하기 (insert) - 특정 위치에 삽입
game.insert(2, "chess")
            
# 2-3. 항목 제거하기 (remove) - 값으로 제거
game.remove("chess")
            
# 2-4. 인덱스로 항목 제거하기 (pop) - 인덱스로 제거
game.pop(0)            
            
# 2-5. 항목 찾기 (index) - 값의 인덱스 반환
game.index("battlegrounds")

# 2-6. 리스트 슬라이싱
          
# 3. Tuple (튜플)
#튜플은 리스트와 비슷하지만, 값이 변경되지 않는 변경 불가능한(immutable) 데이터 타입입니다.
