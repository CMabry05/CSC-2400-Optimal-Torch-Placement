# Cell symbols
UNLIT, LIT, WALL, TORCH = '0', '1', 'x', 'T'

# A torch emits light level 14, losing 1 per block of distance. Mobs can't
# spawn at light level 1+, so a torch covers blocks up to 13 steps away.
TORCH_LEVEL = 7
TORCH_REACH = TORCH_LEVEL - 1


def _has_line_of_sight(grid, a, b):
    """True if no wall sits on the straight line between the centres of a and b."""
    (r1, c1), (r2, c2) = a, b
    steps = 4 * max(abs(r2 - r1), abs(c2 - c1), 1)
    for i in range(1, steps):
        t = i / steps
        r = int(r1 + 0.5 + (r2 - r1) * t)   # cell containing the sample point
        c = int(c1 + 0.5 + (c2 - c1) * t)
        if (r, c) not in (a, b) and grid[r][c] == WALL:
            return False
    return True


def _light_area(grid, torch, reach=TORCH_REACH):
    """
    Cells lit by a torch at `torch`: Minecraft's diamond shape
    (Manhattan distance <= reach), minus anything a wall blocks.
    Walls themselves are never lit.
    """
    rows, cols = len(grid), len(grid[0])
    tr, tc = torch
    area = set()
    for r in range(max(0, tr - reach), min(rows, tr + reach + 1)):
        for c in range(max(0, tc - reach), min(cols, tc + reach + 1)):
            if abs(r - tr) + abs(c - tc) > reach:      # outside the diamond
                continue
            if grid[r][c] == WALL:
                continue
            if _has_line_of_sight(grid, torch, (r, c)):
                area.add((r, c))
    return area


def place_torches(grid, reach=TORCH_REACH):
    """
    Place the fewest (greedy) extra torches so no reachable '0' cell stays unlit.

    grid  : list of lists (or list of strings) using '0', '1', 'x', 'T'
    reach : torch light distance in blocks (default 13)

    Returns (new_grid, torch_positions). Newly placed torches are 'T'; only
    cells actually lit by a torch (diamond shape, not behind walls) become '1'.
    """
    g = [list(row) for row in grid]
    rows, cols = len(g), len(g[0])
    cells = [(r, c) for r in range(rows) for c in range(cols)]

    # Light from existing torches
    for r, c in cells:
        if g[r][c] == TORCH:
            for lr, lc in _light_area(g, (r, c), reach):
                if g[lr][lc] == UNLIT:
                    g[lr][lc] = LIT

    # uncovered = {(r, c) for r, c in cells if g[r][c] == UNLIT}
    # candidates = [(r, c) for r, c in cells if g[r][c] in (UNLIT, LIT)]
    # coverage = {p: _light_area(g, p, reach) for p in candidates}

    # placed = []
    # while uncovered:
    #     best = max(candidates, key=lambda p: len(coverage[p] & uncovered))
    #     placed.append(best)
    #     uncovered -= coverage[best]
    #     for lr, lc in coverage[best]:
    #         if g[lr][lc] == UNLIT:
    #             g[lr][lc] = LIT
    #     candidates.remove(best)

    # for r, c in placed:
    #     g[r][c] = TORCH
    # return g, placed


def remove_torch(grid, pos, reach=TORCH_REACH):
    """
    Remove the torch at `pos` and unlight only the cells that no other torch
    still lights. Cells shared with other torches stay '1'.

    grid  : list of lists (or list of strings)
    pos   : (row, col) of the torch to remove
    reach : torch light distance in blocks (default 13)

    Returns a new grid. Raises ValueError if there is no torch at `pos`.
    Note: the grid can't tell torch light from other light sources, so any
    '1' cell inside the removed torch's area that no remaining torch covers
    is set to '0'.
    """
    g = [list(row) for row in grid]
    r0, c0 = pos
    if g[r0][c0] != TORCH:
        raise ValueError(f"No torch at {pos}")

    # What the removed torch was lighting (computed with it still in place)
    removed_area = _light_area(g, pos, reach)

    # Take the torch out; its own cell becomes a normal open cell
    g[r0][c0] = LIT

    # Everything the remaining torches still light
    still_lit = set()
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == TORCH:
                still_lit |= _light_area(g, (r, c), reach)

    # Unlight only cells that were lit by the removed torch and nothing else
    for r, c in removed_area:
        if g[r][c] == LIT and (r, c) not in still_lit:
            g[r][c] = UNLIT
    return g


if __name__ == "__main__":
    room = [
        "0000000000000000000000000000",
        "0000000000000000000000000000",
        "00000000xxxxxxxx000000000000",
        "00000000x000000x000000000000",
        "00000000x000000x000000000000",
        "000000000000000x000000000000",
        "0000000000000000000000000000",
        "1100000000000000000000000000",
    ]
    #result, torches = place_torches(room)
    #print("\n".join("".join(row) for row in result))
    #print(f"\nPlaced {len(torches)} torches at (row, col): {torches}")

    # Sanity check: a torch next to a wall must not light the far side
    wall_test = ["00x00", "00x00", "00x00"]
    #res, t = place_torches(["00x0T", "00x00", "00x00"], reach=3)
    print()
    #print("\n".join("".join(row) for row in res))
