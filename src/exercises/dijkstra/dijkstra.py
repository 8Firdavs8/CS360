#!/usr/bin/env python3
"""Diykstra's algorithm usage"""


from pythonds3.graphs import Graph
import toml


def read_toml(filename: str) -> Graph:
    """Read TOML config file"""
    new_dir, graph =  dict(), Graph()
    route = toml.load(filename)
    for x in route['routers']: 
        new_dir[x['address']] = x['name']
    for x in route['routers']:
        for y in x['neighbors']: 
            graph.add_edge(x['name'], new_dir[y['address']], y['cost'])
    return graph


def find_path(g: Graph, start: str) -> None:
    """Use Diykstra's algorithm to find the shortest path from start to other vertices"""
    print(g.dijkstra(g.get_vertex(start)))
    



def main():
    pass


if __name__ == "_main_":
    main()
