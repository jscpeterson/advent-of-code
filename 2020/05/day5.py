def get_data(filepath):
    return [line.strip('\n') for line in open(filepath).readlines()]

bin_trans = str.maketrans({'F':'0', 'B':'1', 'R':'1', 'L':'0'})

def get_seats(inputs):
    seats = []
    for boarding_pass in inputs:
        row = boarding_pass[:7]
        col = boarding_pass[7:]
        seat = int(row.translate(bin_trans), 2) * 8 + int(col.translate(bin_trans), 2)
        seats.append(seat)
    return seats

assert get_seats(get_data('test')) == [567, 119, 820]
seats = get_seats(get_data('input'))
print('Part 1: %s' % max(seats))

def find_seat(seats):
    seats.sort()
    for seat in range(seats[0], seats[len(seats)-1]):
        if seat not in seats:
            return seat

print('Part 2: %s' % find_seat(seats))
