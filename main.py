import vessel
import cover
import policy

# Lets create and add vessels to policy
vessels = [vessel.Vessel("Maersk Jaqueline", "222222222"), vessel.Vessel("Maersk Cormac", "411411411")]

# Lets create the policy
maersk_policy = policy.Policy("Corcoran Main", "01/01/1988", "31/12/1988")

# create some covers and add to policy
covers = [cover.CoverType("Hull & Machinery", 0.365), cover.CoverType("War", 0.01)]

# add the assets and covers  to the policy
maersk_policy.add_assets(vessels)
maersk_policy.add_covers(covers)

# Display policy details
maersk_policy.display_details()
