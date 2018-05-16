def load_num(filename):
    """
    Load variables x0, v0, t, h from a plain-text file and return these 
	 as a list.
    """
    with open(filename) as vari:
        A0 = vari.read().split()
        A1 = []
        for i in A0:
            i1 = float(i)
            A1.append(i1)
        return A1