from tile_map import TileMap

tm = TileMap(8, 8)

tm.set_init_point([7, 0])
tm.set_pack_point([0, 4])
tm.set_end_point([7, 5])

tm.printM()

shortest_path = tm.find_shortest_path()
print(shortest_path)
