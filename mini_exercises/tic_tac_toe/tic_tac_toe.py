def print_grid(grid):
    for idx, row in enumerate(grid):
        new_row = list(row.values())
        if idx == 0:
            print(f" 2  {new_row}")
        elif idx == 1:
            print(f" 1  {new_row}")
        else:
            print(f" 0  {new_row}")
    print("      A    B    C")


def turn_input(player_symbol, chosen_values):
    allowed_values = ["a0", "a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2"]
    tile = ""
    if player_symbol == "x":
        while not tile:
            response = (
                input(
                    "Player's 1 turn you place 'x'. Choose a tile /example (a2, b0, c1): "
                )
                .strip()
                .lower()
            )

            if response not in allowed_values:
                print("wrong value! try again")

            elif response in chosen_values:
                print("The given value has already been chosen. Try a different one.")

            else:
                tile = response

    elif player_symbol == "o":
        while not tile:
            response = (
                input(
                    "Player's 2 turn you place 'o'. Choose a tile /example (a2, b0, c1): "
                )
                .strip()
                .lower()
            )

            if response not in allowed_values:
                print("wrong value! try again")

            elif response in chosen_values:
                print("The given value has already been chosen. Try a different one.")

            else:
                tile = response

    return response


def assign_tile_to_a_grid(tile_to_change, grid, player_symbol):
    new_grid = list(grid)
    s = tile_to_change.strip().lower()
    for idx, row in enumerate(grid):
        if not s in row:
            continue

        n_row = dict(row)
        n_row[s] = player_symbol
        new_grid[idx] = n_row
        break

    return new_grid


def check_winner(grid, player_symbol):
    if player_symbol == "x":
        winner = "Player_1"
    elif player_symbol == "o":
        winner = "Player_2"

    columns = [[], [], []]
    for row in grid:
        for k, v in row.items():
            if "a" in k:
                columns[0].append(v)
            elif "b" in k:
                columns[1].append(v)
            else:
                columns[2].append(v)

    count_1 = 0
    r_grid = list(grid)
    r_grid.reverse()
    for idx, row in enumerate(grid):
        new_row = list(row.values())

        # check rows
        if new_row[0] != "_" and new_row[0] == new_row[1] == new_row[2]:
            return f"Congratulations!!!\n{winner} wins!\nFound 3 '{player_symbol}'s in a row."

        # checks diagonal
        if new_row[idx] != player_symbol:
            continue
        else:
            count_1 += 1

    count_2 = 0
    for idx, row in enumerate(r_grid):
        new_row = list(row.values())
        if new_row[idx] != player_symbol:
            continue
        else:
            count_2 += 1

    if count_1 == 3 or count_2 == 3:
        return f"Congratulations!!!\n{winner} wins!\nFound 3 '{player_symbol}'s diagonally."

    for col in columns:
        # check columns
        if col[0] != "_" and col[0] == col[1] == col[2]:
            return f"Congratulations!!!\n{winner} wins!\nFound 3 '{player_symbol}'s in a column."


def main():
    p_1_symbol = "x"
    p_2_symbol = "o"

    a0 = "_"
    a1 = "_"
    a2 = "_"

    b0 = "_"
    b1 = "_"
    b2 = "_"

    c0 = "_"
    c1 = "_"
    c2 = "_"

    grid = [
        {"a2": a2, "b2": b2, "c2": c2},
        {"a1": a1, "b1": b1, "c1": c1},
        {"a0": a0, "b0": b0, "c0": c0},
    ]

    winner = ""
    players_turn = "player_1"
    chosen_values = []

    print_grid(grid)
    while not winner:
        if len(chosen_values) == 9:
            winner = "Game ends, it's a draw!"
            break
        if players_turn == "player_1":
            tile_to_change = turn_input(p_1_symbol, chosen_values)
            chosen_values.append(tile_to_change)
            players_turn = "player_2"
            grid = assign_tile_to_a_grid(tile_to_change, grid, p_1_symbol)
            print_grid(grid)
            winner = check_winner(grid, p_1_symbol)
            if winner:
                break

        elif players_turn == "player_2":
            tile_to_change = turn_input(p_2_symbol, chosen_values)
            chosen_values.append(tile_to_change)
            players_turn = "player_1"
            grid = assign_tile_to_a_grid(tile_to_change, grid, p_2_symbol)
            print_grid(grid)
            winner = check_winner(grid, p_2_symbol)
            if winner:
                break
    print(winner)


if __name__ == "__main__":
    main()
