# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:58:50 2016
Author: RP
"""

import serpent
from ethereum import tester as t, utils as u, abi

s = t.state()
c = s.abi_contract("multiauth_limits.se")

# Create limit accounts and query contents
c.init_limit(0, 100, 1000)
c.ask_limit(0)
c.ask_balance(0)
c.ask_sender(0)
c.init_limit(1, 500, 1000)
c.ask_limit(1)
c.ask_balance(0)
c.ask_sender(1)

# Transfer
b00 = c.transfer(0, 100) # Valid
b01 = c.transfer(0,901) # Invalid, since results in negative balance

b1 = c.transfer(1, 501) #Invalid, since above user 1's limit of 500