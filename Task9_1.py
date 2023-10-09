dna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}

def change(s):

    def sp(s):
        return [elem for elem in s]

    s = sp(s)
    cs = [dna[i] for i in s]
    result = ''.join(cs)
    return result

s = str(input())
print(change(s))