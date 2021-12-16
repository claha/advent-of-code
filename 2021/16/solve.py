"""Advent Of Code #16."""
from functools import reduce

with open("input") as f:
    data = f.read().strip()
packet = "{:b}".format(int(data, 16))
packet = "0" * (len(data) * 4 - len(packet)) + packet


class Packet:
    """Representation of a packet."""

    def __init__(self, packet):
        """Create a packet."""
        self.packet = packet
        self.versions = []

    def decode_bits(self, bits):
        """Decode a number of bits of the packet."""
        value = int(self.packet[0:bits], 2)
        self.packet = self.packet[bits:]
        return value

    def decode_version(self):
        """Decode version."""
        version = self.decode_bits(3)
        self.versions.append(version)

    def decode_type_id(self):
        """Decode type id."""
        return self.decode_bits(3)

    def decode_value(self):
        """Decode value."""
        value = 0
        while self.decode_bits(1) == 1:
            value += self.decode_bits(4)
            value <<= 4
        value += self.decode_bits(4)
        return value

    def decode_length_type_id(self):
        """Decode length type id."""
        return self.decode_bits(1)

    def decode_total_length(self):
        """Decode total length."""
        return self.decode_bits(15)

    def decode_number_of_sub_packets(self):
        """Decode number of sub packets."""
        return self.decode_bits(11)

    def decode_values(self):
        """Decode values."""
        length_type_id = self.decode_length_type_id()
        if length_type_id == 0:
            total_length = self.decode_total_length()
            values = []
            decoded_bits = 0
            while decoded_bits < total_length:
                packet_length = len(self.packet)
                value = self.decode()
                values.append(value)
                decoded_bits += packet_length - len(self.packet)
            return values
        else:
            number_of_sub_packets = self.decode_number_of_sub_packets()
            return [self.decode() for _ in range(number_of_sub_packets)]

    def decode(self):
        """Decode."""
        self.decode_version()
        type_id = self.decode_type_id()
        if type_id == 4:
            return self.decode_value()
        else:
            values = self.decode_values()
            if type_id == 0:
                return sum(values)
            elif type_id == 1:
                return reduce(lambda x, y: x * y, values)
            elif type_id == 2:
                return min(values)
            elif type_id == 3:
                return max(values)
            elif type_id == 5:
                assert len(values) == 2
                return int(values[0] > values[1])
            elif type_id == 6:
                assert len(values) == 2
                return int(values[0] < values[1])
            elif type_id == 7:
                assert len(values) == 2
                return int(values[0] == values[1])
            else:
                raise Exception(f"Can not handle {type_id}")


packet = Packet(packet)
value = packet.decode()


# Part 1
print("Part 1:", sum(packet.versions))
assert sum(packet.versions) == 873


# Part 2
print("Part 2:", value)
assert value == 402817863665
