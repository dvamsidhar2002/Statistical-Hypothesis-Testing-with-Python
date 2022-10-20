from scipy.stats import normaltest
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]

stat, p = normaltest(data)

print('stat=%.3f, p=%.3f'%(stat,p))
if p>0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')