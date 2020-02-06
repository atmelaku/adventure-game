class Engine(object):

    def __init__(self, part_map):
        self.part_map = part_map

    def play(self):
        current_part = self.part_map.opening_part()
        last_part = self.part_map.next_part('finished')

        while current_part != last_part:
            next_part_map = current_part.enter()
            current_part = self.part_map.next_part(next_part_map)
        current_part.enter()
