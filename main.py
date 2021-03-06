import vessel
import cover
import policy

# Lets create and add vessels to policy
vessels = [vessel.Vessel("Maersk Jaqueline", "222222222", 26_000_000),
           vessel.Vessel("Maersk Cormac", "411411411", 36_000_000)
           ]
# Lets create the policy
maersk_policy = policy.Policy("Corcoran Main", "01/01/1988", "31/12/1988")

# create some covers and add to policy
covers = [cover.CoverType("Hull & Machinery", 0.263), cover.CoverType("War", 0.014)]

# add the assets and covers  to the policy
maersk_policy.add_assets(vessels)
maersk_policy.add_covers(covers)

# Display policy details
maersk_policy.display_details()

# calculate the premiums on the program
maersk_policy.calculate_premiums()
maersk_policy.display_details()

new_vessel = vessel.Vessel("Martin", "12345678", 20_000_000)

print(new_vessel.value_date)

new_vessel.update_value(10_000_000, "21/03/2021")

print(new_vessel.value)

new_vessel.update_value(30_000_000, "21/03/2021")
print(new_vessel.value)
print(new_vessel.version)

