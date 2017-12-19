ones = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
teens = {
    '0': 'ten',
    '1': 'eleven',
    '2': 'twelve',
    '3': 'thirteen',
    '4': 'fourteen',
    '5': 'fifteen',
    '6': 'sixteen',
    '7': 'seventeen',
    '8': 'eighteen',
    '9': 'nineteen'
}
tens = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}
illions = {
    '1': 'thousand',
    '2': 'million',
    '3': 'billion',
    '4': 'trillion',
    '5': 'quadrillion',
    '6': 'quintillion',
    '7': 'sextillion',
    '8': 'septillion',
    '9': 'octillion'
}

class NumberCount(object):

    def _split_to_sub_arrays(self, number):
        new_arr = []
        consumed_arr = list(str(number))
        sub_arr = []
        while (len(consumed_arr) > 0):
            sub_arr.append(consumed_arr[-1:][0])
            consumed_arr.pop()

            if len(sub_arr) == 3:
                new_arr.append(sub_arr)
                sub_arr = []

        if len(sub_arr) > 0:
            new_arr.append(sub_arr)

        for sub_arr in new_arr:
            sub_arr.reverse()
        return new_arr

    def _name_sub_array(self, arr):
        phrase_arr = []
        for i in range(0,len(arr)):
            if arr[i] == '0':
                continue

            if i == 0:
                if len(arr) == 3:
                    phrase_arr.append('{} hundred'.format(ones.get(arr[i])))
                if len(arr) == 2:
                    if arr[i] == '1':
                        phrase_arr.append('{}'.format(teens.get(arr[i+1])))
                        break
                    phrase_arr.append('{}'.format(tens.get(arr[i])))
                if len(arr) == 1:
                    phrase_arr.append('{}'.format(ones.get(arr[i])))

            if i == 1:
                if len(arr) == 3:
                    if arr[i] == '1':
                        phrase_arr.append('{}'.format(teens.get(arr[i+1])))
                        break
                    phrase_arr.append('{}'.format(tens.get(arr[i])))
                if len(arr) == 2:
                    phrase_arr.append('{}'.format(ones.get(arr[i])))

            if i == 2:
                phrase_arr.append('{}'.format(ones.get(arr[i])))

        return ' '.join(phrase_arr)

    def _find_max_sub_array(self):
        max_sub_name = ''
        max_sub_count = 0

        for i in range(1, 999):
            name = self.name(i)
            count = self.count(name)
            if max_sub_count < count:
                max_sub_count = count
                max_sub_name = name

        return max_sub_name, max_sub_count

    def _print_sub_array_count(self, _count):
        for i in range(1, 999):
            name = self.name(i)
            count = self.count(name)
            if count == _count:
                print(name, count)

    def name(self, number):
        arrs = self._split_to_sub_arrays(number)
        number_arr = []
        for i in range(0, len(arrs)):
            named = self._name_sub_array(arrs[i])
            if i > 0:
                named = named + ' ' + illions.get(str(i), '')
            number_arr.append(named)
        number_arr.reverse()
        return ' '.join(number_arr) + '!'

    def count(self, phrase):
        return len(phrase)


nc = NumberCount()
print "nc = NumberCount()"
print "Find max sub phrase ->"
max_sub_phrase, max_sub_count = nc._find_max_sub_array()
print "max_sub_phrase, max_sub_count = nc._find_max_sub_array()"
print "max_sub_phrase -> {}".format(max_sub_phrase)
print "build number until limit hit -> 373373373373373373373373"
print "Count: {}".format(nc.count(nc.name(373373373373373373373373)))
print "find sub_phrases that hit limit 293 - 280 + spaces (2) = 15"
print "nc._print_sub_array_count(16) # `!` included so limit + 1"
nc._print_sub_array_count(16)
print "minimum in list -> 'one hundred one'"
print "replace beginning sub phrase with minimum value in phrase list"
print "max_after_limit = 101373373373373373373373"
print "one less -> 101373373373373373373372"
max_before_limit = 101373373373373373373372

name = nc.name(max_before_limit)
count = nc.count(name)
print "name = nc.name(max_before_limit)"
print "count = nc.count(name)"

print "Name: {}, Count: {}".format(name, count)

#  Smallest so far that breaks 280 101373373373373373373373
