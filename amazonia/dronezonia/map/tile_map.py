import heapq

# from tile import Tile
from .tile import Tile


class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.init_point = None
        self.pack_point = None
        self.end_point = None
        self.path = []
        self.found = False
        # Create a tiles matrix
        self.tiles_matrix = [
            [Tile(x + y * width + 1, y, x) for x in range(self.height)] for y in range(self.width)]
        self.costs_matrix = [
            [float('inf') for _ in range(self.height)] for _ in range(self.width)]
        self.init_matrix()

    def init_matrix(self):
        for row in range(self.height):
            for col in range(self.width):
                self.set_neighbors(row, col)
                self.tiles_matrix[row][col].init_cost()

    def reset_matrix(self):
        for row in range(self.height):
            for col in range(self.width):
                self.costs_matrix[row][col] = float('inf')
                self.tiles_matrix[row][col].previous = None

    def convert_number_to_letter(number):
        letter = chr(number + 65)  # 65 é o código Unicode para a letra 'A'
        return letter

    def convert_letter_to_number(self, letter):
        # Converte a letra para um número de coluna (0 é o código Unicode para 'A')
        column = ord(letter[0].upper()) - 65
        # Converte o número da linha para um índice e subtrai 1
        row = int(letter[1:]) - 1

        return row, column

    def get_chess_table(self):
        chess_table = {}
        for row in range(self.height):
            for col in range(self.width):
                tile = self.tiles_matrix[row][col]
                tile_str = str(tile)  # Converte o tile para string

                neighbors_dict = {}
                for neighbor in tile.neighbors:
                    # Converte o vizinho para string
                    neighbor_str = str(neighbor)
                    # Adiciona vizinho e custo ao dicionário de vizinhos
                    neighbors_dict[neighbor_str] = neighbor.cost

                chess_table[tile_str] = neighbors_dict

        return chess_table

    def set_neighbors(self, row, col):
        tile = self.tiles_matrix[row][col]
        if row > 0:
            nei = self.tiles_matrix[row-1][col]
            tile.neighbors.append(nei)
        if col > 0:
            nei = self.tiles_matrix[row][col-1]
            tile.neighbors.append(nei)
        if row < self.width-1:
            nei = self.tiles_matrix[row+1][col]
            tile.neighbors.append(nei)
        if col < self.height-1:
            nei = self.tiles_matrix[row][col+1]
            tile.neighbors.append(nei)

    def set_init_point(self, point):
        self.init_point = point

    def set_pack_point(self, point):
        self.pack_point = point

    def set_end_point(self, point):
        self.end_point = point

    def printM(self):
        for x in range(self.width):
            print("")
            for y in range(self.height):
                print(self.tiles_matrix[x][y].cost, end='')
        print("")

    def printM2(self):
        for x in range(self.width):
            print("")
            for y in range(self.height):
                print(self.costs_matrix[x][y], end=' ')
        print("")

    def dijkstra(self, start, end, initial_cost=0):
        # Initialize the costs matrix
        self.costs_matrix[start[0]][start[1]] = initial_cost
        initial_tile = self.tiles_matrix[start[0]][start[1]]

        # Create a heap with the starting node
        heap = [(initial_cost, self.tiles_matrix[start[0]][start[1]])]

        while heap:
            # Get the node with the smallest cost
            (current_cost, current_node) = heapq.heappop(heap)

            # Check if we already visited this node
            if current_node.visited:
                continue

            # Mark the node as visited
            current_node.visited = True

            # Check if we reached the end node
            goal_tile = self.tiles_matrix[end[0]][end[1]]

            # Update the costs to move to the neighbors
            for neighbor in current_node.neighbors:
                if neighbor.visited:
                    continue

                new_cost = current_cost + neighbor.cost
                neighbor_cost = self.costs_matrix[neighbor.row][neighbor.col]

                if new_cost < neighbor_cost:
                    self.costs_matrix[neighbor.row][neighbor.col] = new_cost
                    neighbor.previous = current_node
                    neighbor.dist = current_cost
                    heapq.heappush(heap, (new_cost, neighbor))

        # Reset the visited flag for all nodes
        for row in self.tiles_matrix:
            for node in row:
                node.visited = False

        # Build the path from start to end
        path = []
        current_node = self.tiles_matrix[end[0]][end[1]]
        while current_node.previous is not None:
            cost = round((current_node.dist + current_node.cost), 2)
            tile_dict = current_node.as_dict()
            path.append((current_node.id, current_node.row,
                        current_node.col, cost))
            current_node = current_node.previous

        path.append((initial_tile.id, initial_tile.row,
                    initial_tile.col, initial_cost))
        path.reverse()

        return path

    def find_shortest_path(self):
        # Find the shortest path from I to P
        path1 = self.dijkstra(self.init_point, self.pack_point)

        print(path1)

        self.reset_matrix()
        # get the cost to the pack to be the starter cost in the second part of the path
        initial_cost = path1[-1][2]
        # Find the shortest path from P to E
        path2 = self.dijkstra(self.pack_point, self.end_point, initial_cost)

        # Combine two paths
        path = path1[:-1] + path2

        self.reset_matrix()
        for step in path:
            self.costs_matrix[step[1]][step[2]] = 11

        self.printM2()

        return path

    def fill_with_data(self, data):
        table = data.get("table", None)
        for t in table:
            print(self.convert_letter_to_number(t))
