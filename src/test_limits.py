# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:58:50 2016

@author: https://github.com/mc2-umd/ethereumlab/blob/master/Examples/mutual_credit_system.py
"""

import serpent
from ethereum import tester as t, utils as u, abi

#%%

# From original UofM tutorial
public_k0 = u.privtoaddr(t.k0)
public_k1 = u.privtoaddr(t.k1)
print("whassup")


s = t.state()
c = s.abi_contract("multiauth_limits.se")


#
#o = c.balance(public_k0)
#print("tester.k0's current balance is " + str(o))
#
#o = c.balance(public_k1)
#print("tester.k1's current balance is " + str(o))
#
#o = c.transfer(public_k0, 500, sender=tester.k1)
#if o == 1:
#	print("500 credits sent to tester_k1 from tester_k0")
#else:
#	print("Failed to send 500 credits to tester_k1 from tester_k0")
#
#o = c.balance(public_k0)
#print("tester.k0's current balance is " + str(o))
#
#o = c.balance(public_k1)
#print("tester.k1's current balance is " + str(o))
#
#o = c.transfer(public_k0, 1500, sender=tester.k1)
#if o == 1:
#	print("1500 credits sent to tester_k1 from tester_k0")
#else:
#	print("Failed to send 1500 credits to tester_k1 from tester_k0")
#
#o = c.transfer(public_k0, 500, sender=tester.k1)
#if o == 1:
#    print("500 credits sent to tester_k1 from tester_k0")
#else:
#    print("Failed to send 500 credits to tester_k1 from tester_k0")
#
#o = c.balance(public_k0)
#print("tester.k0's current balance is " + str(o))
#
#o = c.balance(public_k1)
#print("tester.k1's current balance is " + str(o))