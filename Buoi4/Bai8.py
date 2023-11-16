def play_game():
    player1_wins = []
    player2_wins = []
    player1_penalty = 0
    player2_penalty = 0
    round_number = 1

    while True:
        print("Round", round_number)
        n = int(input("Nhập số nguyên dương n: "))
        k = int(input("Nhập số nguyên dương k (n > k): "))

        while n <= k:
            print("n phải lớn hơn k. Vui lòng nhập lại.")
            n = int(input("Nhập số nguyên dương n: "))
            k = int(input("Nhập số nguyên dương k (n > k): "))

        current_player = 1

        while True:
            if current_player == 1:
                print("Lượt của người chơi 1")
            else:
                print("Lượt của người chơi 2")

            move = int(input("Nhập số nguyên dương trong đoạn [1, {}]: ".format(min(n, k))))

            while move < 1 or move > min(n, k):
                print("Số không hợp lệ. Vui lòng nhập lại.")
                move = int(input("Nhập số nguyên dương trong đoạn [1, {}]: ".format(min(n, k))))

            if current_player == 1:
                n -= move
                if n <= 0:
                    player1_wins.append(round_number)
                    break
                current_player = 2
            else:
                n -= move
                if n <= 0:
                    player2_wins.append(round_number)
                    break
                current_player = 1

        print("Người chơi {} thắng round {}.".format(current_player, round_number))

        play_again = input("Bạn có muốn tiếp tục chơi? (YES/NO): ")

        while play_again != "YES" and play_again != "NO":
            play_again = input("Vui lòng nhập YES hoặc NO: ")

        if play_again == "NO":
            break

        round_number += 1

    if len(player1_wins) > len(player2_wins):
        print("Người chơi 1 thắng chung cuộc.")
    elif len(player1_wins) < len(player2_wins):
        print("Người chơi 2 thắng chung cuộc.")
    else:
        if player1_penalty > player2_penalty:
            print("Người chơi 2 thắng chung cuộc.")
        elif player1_penalty < player2_penalty:
            print("Người chơi 1 thắng chung cuộc.")
        else:
            print("Hòa cuộc.")

    print("Round mà người chơi 1 thắng:", player1_wins)
    print("Round mà người chơi 2 thắng:", player2_wins)


play_game()