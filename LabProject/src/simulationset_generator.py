import numpy as np
d
def avoid_the_same_value_func(x, y):
	for i in range(len(x)):
		if x[i] == y[i]:
			x[i]+=0.001
	return (x, y)

def curve_simulation_func(x, a=1):
	# y = ax^2
	delta = np.random.uniform(-0.05, 0.05, size=(len(x),))
	y = a * x * x + delta
	return y

def linear_simulation_func(x, a=1, b = 0):
	# y = ax + b
	np.random.seed(1)
	delta = np.random.uniform(-0.05, 0.05, size=(len(x),))
	y = a * x + delta + b
	return y

def normalize_func(x):
    maxval = np.max(x)
    minval = np.min(x)
    normalized_val = (x-minval)/(maxval-minval)
    return normalized_val

def normalize_to_target_range_func(x, rStart, rStop):
    maxval = np.max(x)
    minval = np.min(x)
    A = np.array([[1,rStop],[1,rStart]])
    B = np.array([[maxval],[minval]])
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    ans_x, ans_y = ans[0, 0], ans[1, 0]
    normalized_val = (x-ans_x)/ans_y
    return normalized_val

def create_normal_data(mu, sigma, size):
    """create independent normal simulation set"""
    np.random.seed(1)
    x = np.round(np.random.normal(mu, sigma, size), 6)
    y = np.round(np.random.normal(mu, sigma, size), 6)
    return (x, y)

def create_exponential_data(scale, size):
    """create independent exponential simulation set"""
    np.random.seed(1)
    x = np.random.exponential(scale, size)
    y = np.random.exponential(scale, size)
    return (x, y)

def create_bimodal_subdata(mu, sigma, size, rStart, rStop):
    """create independent bimodal simulation subdata"""
    x, y = create_normal_data(mu, sigma, size)
    x = normalize_to_target_range_func(x, rStart, rStop)
    y = normalize_func(y)
    return (x, y)

def merge_subset_data(subset1_x, subset1_y, subset2_x, subset2_y):
    """merge the two subset data"""
    x = np.concatenate((subset1_x, subset2_x), axis=0)
    y = np.concatenate((subset1_y, subset2_y), axis=0)
    return (x, y)

def create_bimodal_data():
    """create independent bimodal simulation data"""
    np.random.seed(1)
    # create subset1 data
    mu, sigma, size = 80, 10, 250
    subset1_x, subset1_y = create_bimodal_subdata(mu, sigma, size, rStart=0.45, rStop=1)
    # create subset2 data
    mu, sigma, size = 20, 10, 250
    subset2_x, subset2_y = create_bimodal_subdata(mu, sigma, size, rStart=0, rStop=0.55)
    # merge
    x, y = merge_subset_data(subset1_x, subset1_y, subset2_x, subset2_y)
    return (x, y)

def create_indepComplex_data():
    """create independent complex simulation data"""
    np.random.seed(1)
    mu, sigma, size = 0, 1, 125
    #sub set1
    x1, y1 = create_normal_data(mu, sigma, size)
    x1 = normalize_to_target_range_func(x1, 0.45, 1)
    y1 = normalize_to_target_range_func(y1, 0.45, 1)
    #sub set2
    x2, y2 = create_normal_data(mu, sigma, size)
    x2 = normalize_to_target_range_func(x2, 0.45, 1)
    y2 = np.abs(y2)
    y2 = normalize_to_target_range_func(y2, 0, 0.55)
    #sub set3
    x3, y3 = create_normal_data(mu, sigma, size)
    x3 = np.abs(x3)
    x3 = normalize_to_target_range_func(x3, 0, 0.55)
    y3 = normalize_to_target_range_func(y3, 0.45, 1)
    #sub set4
    x4, y4 = create_normal_data(mu, sigma, size)
    x4 = np.abs(x4)
    x4 = normalize_to_target_range_func(x4, 0, 0.55)
    y4 = np.abs(y4)
    y4 = normalize_to_target_range_func(y4, 0, 0.55)
    #merge
    x5 = np.concatenate((x1, x2, x3, x4), axis=0)
    y5 = np.concatenate((y1, y2, y3, y4), axis=0)
    return (x5, y5)

def create_linear_positive_data():
    """create partial dependent positive linear simulation data"""
    np.random.seed(1)
    #create 250 linear set
    x1 = np.linspace(0, 1, 250)
    y1 = linear_simulation_func(x1)
    x1 = normalize_func(x1)
    y1 = normalize_func(y1)
    #create 250 random set
    x2 = np.random.random_sample((250,))
    y2 = np.random.random_sample((250,))
    x2 = normalize_func(x2)
    y2 = normalize_func(y2)
    #merge
    x3 = np.concatenate((x1, x2), axis=0)
    y3 = np.concatenate((y1, y2), axis=0)
    return (x3, y3)

def create_linear_negative_data():
    """create partial dependent negative linear simulation data"""
    np.random.seed(1)
    #create 250 linear set
    x1 = np.linspace(0, 1, 250)
    y1 = linear_simulation_func(x1, a=-1, b=1)
    x1 = normalize_func(x1)
    y1 = normalize_func(y1)
    #create 250 random set
    x2 = np.random.random_sample((250,))
    y2 = np.random.random_sample((250,))
    x2 = normalize_func(x2)
    y2 = normalize_func(y2)
    #merge
    x3 = np.concatenate((x1, x2), axis=0)
    y3 = np.concatenate((y1, y2), axis=0)
    return (x3, y3)

def create_partial_nonlinear_data():
    """create partial dependent nonlinear simulation data"""
    np.random.seed(1)
    #create 250 linear set
    x1 = np.linspace(-1, 1, 250)
    y1 = curve_simulation_func(x1, a=-1)
    x1 = normalize_func(x1)
    y1 = normalize_func(y1)
    #create 250 random set
    x2 = np.random.random_sample((250,))
    y2 = np.random.random_sample((250,))
    x2 = normalize_func(x2)
    y2 = normalize_func(y2)
    #merge
    x3 = np.concatenate((x1, x2), axis=0)
    y3 = np.concatenate((y1, y2), axis=0)
    return (x3, y3)

def create_partComplex_data():
    """create partial dependent complex simulation data"""
    np.random.seed(1)
    #creat 125 linear set
    x1 = np.linspace(0, 1, 125)
    y1 = linear_simulation_func(x1, a=1, b=0)
    x1 = normalize_func(x1)
    y1 = normalize_func(y1)
    #creat 125 linear set
    x2 = np.linspace(0, 1, 125)
    y2 = linear_simulation_func(x1, a=-1, b=1)
    x2 = normalize_func(x2)
    y2 = normalize_func(y2)
    #creat 250 random set
    x3 = np.random.random_sample((250,))
    y3 = np.random.random_sample((250,))
    x3 = normalize_func(x3)
    y3 = normalize_func(y3)
    #merge
    x4 = np.concatenate((x1, x2, x3), axis=0)
    y4 = np.concatenate((y1, y2, y3), axis=0)
    return (x4, y4)

def create_linear_data():
    """create dependent linear simulation data"""
    np.random.seed(1)
    x = np.linspace(0, 1, 500)
    y = linear_simulation_func(x)
    return (x, y)

def create_nonlinear_data():
    """create dependent nonlinear simulation data"""
    np.random.seed(1)
    x = np.linspace(-1, 1, 500)
    y = curve_simulation_func(x, a=-1)
    return (x, y)

def create_piecewise_linear_data():
    """create dependent piecewise linear simulation data"""
    np.random.seed(1)
    #sub set1
    x1 = np.linspace(0, 0.25, 125)
    y1 = linear_simulation_func(x1, a=1)
    y1 = normalize_to_target_range_func(y1, 0.0, 0.75)
    #sub set2
    x2 = np.linspace(0.25, 0.75, 250)
    y2 = linear_simulation_func(x2, a=-1)
    y2 = normalize_to_target_range_func(y2, 0.25, 0.75)
    #sub set3
    x3 = np.linspace(0.75, 1, 125)
    y3 = linear_simulation_func(x3, a=1)
    y3 = normalize_to_target_range_func(y3, 0.25, 1)
    #merge
    x4 = np.concatenate((x1,x2,x3), axis=0)
    y4 = np.concatenate((y1,y2,y3), axis=0)
    return (x4, y4)

def create_depComplex_data():
    """create dependent complex simulation data"""
    np.random.seed(1)
    #sub set1
    mu, sigma, size = 80, 10, 250
    x1 = np.round(np.random.normal(mu, sigma, size), 6)
    y1 = np.round(np.random.normal(mu, sigma, size), 6)
    #sub set2
    mu, sigma, size = 20, 10, 250
    x2 = np.round(np.random.normal(mu, sigma, size), 6)
    y2 = np.round(np.random.normal(mu, sigma, size), 6)
    #merge
    x3 = np.concatenate((x1, x2), axis = 0)
    y3 = np.concatenate((y1, y2), axis = 0)
    return (x3, y3)

class simulationset_generator():

    def __init__(self, mu=0, sigma=0.1, size=500, scale=1.0):
        self.mu = mu
        self.sigma = sigma
        self.size = size
        self.scale = scale

    def create_normal_set(self):
        return create_normal_data(self.mu, self.sigma, self.size)

    def create_exponential_set(self):
        return create_exponential_data(self.scale, self.size)

    def create_bimodal_set(self):
        return create_bimodal_data()

    def create_indepComplex_set(self):
        return create_indepComplex_data()

    def create_linear_positive_set(self):
        return create_linear_positive_data()

    def create_linear_negative_set(self):
        return create_linear_negative_data()
        
    def create_partial_nonlinear_set(self):
        return create_partial_nonlinear_data()

    def create_partComplex_set(self):
        return create_partComplex_data()

    def create_linear_set(self):
        return create_linear_data()
    
    def create_nonlinear_set(self):
        return create_nonlinear_data()

    def create_piecewise_linear_set(self):
        return create_piecewise_linear_data()

    def create_depComplex_set(self):
        return create_depComplex_data()