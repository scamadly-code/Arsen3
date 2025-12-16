import chess
import chess.svg

def print_board(board):
    # Виводимо поточну дошку в текстовому вигляді
    print(board)

def play_game():
    board = chess.Board()  # Створюємо нову шахову дошку
    print("Час почати гру!")
    print_board(board)

    while not board.is_game_over():  # Гра триває, поки не буде мату або нічиї
        print("Тепер твій хід!")
        move = input("Введи хід (наприклад, 'e2e4'): ").strip()
        



        
        # Перевірка, чи є хід правильним
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))  # Виконуємо хід
            print_board(board)  # Виводимо оновлену дошку
        else:
            print("Невірний хід. Спробуй ще раз.")

    print("Гра завершена!")
    print("Результат:", board.result())  # Показуємо результат партії

if __name__ == "__main__":
    play_game()