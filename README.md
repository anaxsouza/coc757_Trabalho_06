# coc757_Trabalho_05
 
Resolver os problemas computacionais 9.2 e 9.3 da última edição do livro texto: 
Heath M.T - Scientific computing_ an introductory survey-SIAM (2018)

# Problema 1:

The Kermack-McKendrick model for the course of an epidemic in a population is given by
the system of ODEs

y1' = −c*y1*y2
y2' = c*y1*y2 − d*y2
y3' = d*y2

where y1 represents susceptibles, y2 represents infectives in circulation, 
and y3 represents infectives removed by isolation, death, or recovery and im-
munity. The parameters c and d represent the infection rate and removal rate, 
respectively. Use a library routine to solve this system numerically,
with the parameter values c = 1 and d = 5, and initial values 

y1(0) = 95, y2(0) = 5, y3(0) = 0.

Integrate from t = 0 to t = 1. Plot each solution component on the same graph 
as a function of t. As expected with an epidemic, you should see the number of 
infectives grow at first, then diminish to zero. Experiment with other values for
the parameters and initial conditions. Can you find values for which the epidemic 
does not grow, or for which the entire population is wiped out?

# Problema 2:

Experiment with several different library routines having automatic step-size 
selection to solve the ODE

y' = −200*t*y**2

numerically. Consider two different initial conditions, y(0) = 1 and y(−3) = 1/901, 
and in each case compute the solution until t = 1. Monitor the step size used by the 
routines and discuss how and why it changes as the solution progresses. Ex plain the 
difference in behavior for the two different initial conditions. Compare the different
routines with respect to efficiency for a given accuracy requirement.
