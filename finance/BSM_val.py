import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from BSM_option_valuation import BSM_call_value

mlp.rcParams['font.family'] = 'serif'

Strike_price = 8000
Volatility = 0.2 # constant
Time_to_maturity = 1
Rate = 0.025 # constant riskless rate

# Sample
Index_levels = np.linspace(4000,12000,150)

Intrinsic_values = np.maximum(Index_levels - Strike_price,0)

Call_option_prices = [BSM_call_value(Index_level,Strike_price,0,Time_to_maturity,Rate,Volatility) 
                    for Index_level in Index_levels]

# Graphing
plt.figure()
plt.plot(Index_levels,Intrinsic_values,'b-.',lw=2.5,label='Intrinsic values')
plt.plot(Index_levels,Call_option_prices,'r',lw=2.5,label='Call option values')
plt.grid(True)
plt.legend()
plt.xlabel("Index levels")
plt.ylabel("Present value $C(t=0)$")
plt.show()
