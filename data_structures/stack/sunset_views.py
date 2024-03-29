def sunset_views(buildings, direction):
    building_with_sunset_views = []

    start_idx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    idx = start_idx
    running_max_height = 0

    while 0 <= idx < len(buildings):
        building_height = buildings[idx]

        if building_height > running_max_height:
            building_with_sunset_views.append(idx)

        running_max_height = max(running_max_height, building_height)

        idx += step

    if direction == "EAST":
        return building_with_sunset_views[::-1]  # reverse the list

    return building_with_sunset_views
