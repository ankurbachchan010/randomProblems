def path_count(edge_length):
  if edge_length == 1:
    return 1
  elif edge_length == 0:
    return 0

  total_path_count = 0
  adj_cell = {}
  moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  for i in range(edge_length):
    for j in range(edge_length):
      adj_cell[i,j]= []
      for pos in moves:
        if isValid(i+pos[0],j+pos[1],edge_length):
          adj_cell[i,j].append((i+pos[0],j+pos[1]))

  for startCell in adj_cell:
    for endCell in adj_cell:
      if(startCell != endCell):
          visited = set()
          curr_path_count = [0]
          dfs(visited, adj_cell, startCell, endCell, 0, edge_length, curr_path_count)
          total_path_count = total_path_count + curr_path_count[0]

  return total_path_count

def isValid(i,j, edge_length):
    if i<0 or j<0:
      return False
    elif i>=edge_length or j>=edge_length:
      return False
    else:
      return True

def dfs(visited, adj_cell, currCell, endCell, cell_traversed_count, edge_length, curr_path_count):
  visited.add(currCell)
  cell_traversed_count = cell_traversed_count + 1

  if(currCell == endCell):
    if(cell_traversed_count == edge_length*edge_length):
      curr_path_count[0] = curr_path_count[0] + 1

  for adj in adj_cell[currCell]:
    if(not(adj in visited)):
      dfs(visited, adj_cell, adj, endCell, cell_traversed_count, edge_length, curr_path_count)

  visited.remove(currCell)


if __name__ == '__main__':
  print(path_count(edge_length=4))
