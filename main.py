# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_largest_plot(N, house_numbers_positions):
    # 按照位置对房子进行排序
    house_numbers_positions.sort(key=lambda x: x[1])

    max_gap = 0
    house_pair = (None, None)

    # 遍历计算相邻房子之间的最大间距
    for i in range(1, N):
        current_gap = house_numbers_positions[i][1] - house_numbers_positions[i - 1][1]
        if current_gap > max_gap:
            max_gap = current_gap
            house_pair = (house_numbers_positions[i - 1][0], house_numbers_positions[i][0])
    print(max_gap, house_pair)
    return house_pair

def max_vapor_rate(chemicals):
    n = len(chemicals)
    max_rate = float('-inf')

    for size in range(1, n // 2 + 1):
        for i in range(n - 2 * size + 1):
            first_set = chemicals[i:i + size]
            for j in range(i + size, n - size + 1):
                second_set = chemicals[j:j + size][::-1]

                print(size, i, first_set, second_set)
                total_vapor_rate = sum(first_set[k] * second_set[k] for k in range(size))
                if total_vapor_rate > max_rate:
                    max_rate = total_vapor_rate

    return max_rate if max_rate >= 0 else None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 示例化学品蒸气速率列表
    chemicals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(max_vapor_rate(chemicals))

    # 示例输入
    N = 5
    house_numbers_positions = [(1, 5), (2, 10), (3, 19), (4, 20), (5, 25)]
    print(find_largest_plot(N, house_numbers_positions))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
