def color_graph(build_graph):
# Reorder the nodes by highest to lowest degree.
  graph = sorted(list(build_graph.keys()), key=lambda x: len(build_graph[x]), reverse=True)
  atlas = {}
# For loop to loop through nodes and create list to keep track of which nodes have been visited
  for node in graph:
    vacant_nodes = [True] * len(graph)
# Nested For loop to find all nodes connected to the current node being looked at.
    for adjacent in build_graph[node]:
# If adjacent node is in the dictionary for Set the color's corresponding number to False
      if adjacent in atlas:
        color_list = atlas[adjacent]
        vacant_nodes[color_list] = False
# For loop 
    for color_list, vacant in enumerate(vacant_nodes):
      if vacant:
        atlas[node] = color_list    
        break
  for i, j in atlas.items():
      if j == 0:
        atlas[i] = 'Red'
      elif j == 1:
        atlas[i] = 'Blue'
      elif j == 2:
        atlas[i] = 'Yellow'

  return atlas


if __name__ == '__main__':
  build_graph = {
    '0': list('145'),
    '1': list('034'),
    '2': list('34'),
    '3': list('12'),
    '4': list('0125'),
    '5': list('04')
  }
  print("The colors of each node are,")
  for i, j in color_graph(build_graph).items():
    print("Node:", i, '-', j)