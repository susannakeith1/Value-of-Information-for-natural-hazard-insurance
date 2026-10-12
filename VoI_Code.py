#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for calculating premiums, outcomes and profits, and evaluating 
decisions before and after additional data collection.
"""


def premium(loss, LF):
    """ Calculate the premium required to cover an expected loss
    
    Parameters
    ----------
    loss: Expected loss
    LF: Loading factor applied to the premium
    """
    return loss/(1-LF)


def EFL(x):
    """ Calculate the expected future loss for a given Vs30 value.
    
    Parameters
    ----------
    x: Vs30 value
    
    Returns
    -------
    EFL, expressed as a percentage
    """
    return (-0.001835796 + (0.8056592 - -0.001835796)/(1 + (x/3.107765)**0.5728509))*100



def out(d, x, alpha):
    """ Calculate the client outcome for a given decision and Vs30 value.
    
    Parameters
    ----------
    d: Decision being evaluated (corresponding to the assumed risk (Vs30) value)
    x: Vs30 value
    alpha: Parameter controlling the penalty of uninsuring
    
    """
    if d <= x:
        return -5*EFL(d)/3
    else:
        return -5*EFL(d)/3 -alpha* abs(EFL(d) - EFL(x))


    
def profit(d, x, alpha):
    """ Calculate the insurer outcome for a given client decision and Vs30 value.
    
    Parameters
    ----------
    d: Decision being evaluated (corresponding to the assumed risk (Vs30) value)
    x: Vs30 value
    
    """

    return 5*EFL(d)/3 - min(EFL(x), EFL(d))  # Profit calculation


def prior(x_list, D, n, alpha):
    """Evaluate the optimal decision before additional information is obtained.

    The outcome for each candidate decision is averaged across the n
    possible Vs30 values. The decision with the highest mean outcome
    is selected. The corresponding mean profit is then calculated.

    Parameters
    ----------
    x_list : list
        Possible Vs30 values.
    D : list
        Candidate decisions.
    n : int
        Number of Vs30 values considered.
    alpha : float
        Parameter controlling the penalty in the outcome calculation.

    Returns
    -------
    tuple
        Maximum mean client outcome and mean profit for the selected decision.
    """
    
    listofsum = []
    
    # Calculate the mean client outcome for each candidate decision.  
    for d_i in D:         
        
        summ = 0
        
        for i in range(1, n + 1):
            
            summ += (out(d_i, x_list[i-1], alpha))
            
        total = summ / n
        
        listofsum.append(total)
        
    # Select the decision with the highest mean outcome.   
    maximum = max(listofsum)  
    ind = listofsum.index(maximum)
    d_j = D[ind]     

    # Calculate the mean profit for the selected decision.
    sum_profit = 0
    for i in range(1, n+1):
        sum_profit += profit(d_j, x_list[i-1], alpha)
    
    total_profit = sum_profit / n
    
    return maximum, total_profit



def post(x_list, D, n, alpha):
    """Evaluate decisions when the Vs30 value is known.

    For each possible Vs30 value, select the decision with the highest
    client outcome. Calculate the mean outcome and mean profit across
    all n possible Vs30 values.

    Parameters
    ----------
    x_list : list
        Possible Vs30 values.
    D : list
        Candidate decisions.
    n : int
        Number of Vs30 values considered.
    alpha : float
        Parameter controlling the penalty in the outcome calculation.

    Returns
    -------
    tuple
        Mean of the optimal client outcomes and mean absolute profit.
    """        
    
    total_maxs = 0      
    sum_profit = 0
 
    # Evaluate the optimal decision separately for each possible Vs30 value.
    for i in range(1, n + 1):
        
        listofout = []  
        listofoutp =[]
             
        # Calculate the outcome and profit for every decision
        for d_i in D:       
            listofout.append((out(d_i, x_list[i - 1], alpha)))
            listofoutp.append(profit(d_i, x_list[i - 1], alpha))
               
        # Select the decision that maximises the client outcome
        maxs = max(listofout)
        ind = listofout.index(maxs)
        d_j = D[ind]  
        
        # Accumulate the absolute profit and optimal outcome
        sum_profit += abs(profit(d_j, x_list[i-1], alpha) )
        total_maxs += maxs
        
    # Calculate the mean optimal outcome and mean absolute profit
    total_profit = sum_profit / n        
    final = total_maxs / n
    final_p = total_profit
    
    return final, final_p

